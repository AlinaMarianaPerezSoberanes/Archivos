#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include "filtro.h"
#include "imagen.h"


#define PUERTO 			5000	//Número de puerto asignado al servidor
#define COLA_CLIENTES 	5 		//Tamaño de la cola de espera para clientes
#define TAM_BUFFER 		100
int receive_image(int socket, char nombre[]);
int send_image(int socket, char nombre[]);
void ISRsignal(int sig); //señal de usuario 

char nombreImagen[16]="ImagenS";
char ext[]=".bmp";
char str[12]={};
int  someInt;
char imagenRecibida[15]="Imagen";

//Variables globales
bmpInfoHeader info;
unsigned char *imagenRGB;                    //para leer la imagen a colores en valores RGB dentro de la imagen
unsigned char *imagenGray;                  // en esta imagen se guarda con un tamaño pequeño, cada pixel ocupa 1 byte en memoria
unsigned char *imagenAux;

int main(int argc, char **argv)
{
   	int sockfd, cliente_sockfd;
   	struct sockaddr_in direccion_servidor; //Estructura de la familia AF_INET, que almacena direccion
   	//char leer_mensaje[TAM_BUFFER];
	pid_t pid;    
   
/*	
 *	AF_INET - Protocolo de internet IPV4
 *  htons - El ordenamiento de bytes en la red es siempre big-endian, por lo que
 *  en arquitecturas little-endian se deben revertir los bytes
 *  INADDR_ANY - Se elige cualquier interfaz de entrada
 */	
   	memset (&direccion_servidor, 0, sizeof (direccion_servidor));	//se limpia la estructura con ceros
   	direccion_servidor.sin_family 		= AF_INET;
   	direccion_servidor.sin_port 		= htons(PUERTO); //htons cambia de big indian --> little indian y viceversza
   	direccion_servidor.sin_addr.s_addr 	= INADDR_ANY;

/*
 *	Creacion de las estructuras necesarias para el manejo de un socket
 *  SOCK_STREAM - Protocolo orientado a conexión
 */
   	printf("Creando Socket ....\n");
   	if( (sockfd = socket (AF_INET, SOCK_STREAM, 0)) < 0 ) //sock_stream = socket tcp y regresa el descriptor "sockfd"/Si queremos UDP solo cambiamos SOCK_STREAM
	{
		perror("Ocurrio un problema en la creacion del socket");
		exit(1);
   	}
/*
 *  bind - Se utiliza para unir un socket con una dirección de red determinada
 */
   	printf("Configurando socket ...\n");
   	if( bind(sockfd, (struct sockaddr *) &direccion_servidor, sizeof(direccion_servidor)) < 0 )
	{
		perror ("Ocurrio un problema al configurar el socket");
		exit(1);
   	}
/*
 *  listen - Marca al socket indicado por sockfd como un socket pasivo, esto es, como un socket
 *  que será usado para aceptar solicitudes de conexiones de entrada usando "accept"
 *  Habilita una cola asociada la socket para alojar peticiones de conector procedentes
 *  de los procesos clientes
 */
   	printf ("Estableciendo la aceptacion de clientes...\n");
	if( listen(sockfd, COLA_CLIENTES) < 0 )
	{
		perror("Ocurrio un problema al crear la cola de aceptar peticiones de los clientes");
		exit(1);
   	}
/*
 *  accept - Aceptación de una conexión
 *  Selecciona un cliente de la cola de conexiones establecidas
 *  se crea un nuevo descriptor de socket para el manejo
 *  de la nueva conexion. Apartir de este punto se debe
 *  utilizar el nuevo descriptor de socket
 *  accept - ES BLOQUEANTE 
 */
    if(signal(SIGUSR1, ISRsignal)==SIG_ERR) //creación de la señal de usuario 
    {
        perror("Error al crear la señal\n");
        exit(EXIT_FAILURE);
    }

while(1){
   	printf ("En espera de peticiones de conexión ...\n");
   	if( (cliente_sockfd = accept(sockfd, NULL, NULL)) < 0 ) //accept es bloqueante 
	{
		perror("Ocurrio algun problema al atender a un cliente");
		exit(1);
   	}
	//En esta parte se puede crear un fork para que ese proceso atienda el cliente que se acaba de conectarse
	//posteriormente lo regresamos a que acepte a otro cliente
	
	pid=fork();
	if(!pid){

		//codigo del hijo
		/*
		 *	Inicia la transferencia de datos entre cliente y servidor
		 */
        someInt=getpid();
        //crear el nombre de la imagen con su PID...Nombre unico
        sprintf(str, "%d", someInt);
        strcat(imagenRecibida,str);
        strcat(imagenRecibida,ext);
        printf("%s",imagenRecibida);
    
		receive_image(cliente_sockfd, imagenRecibida);
		int *hilo,i,k,nhs[NUM_HILOS];                                            //Arreglo de hilos
    	pthread_t tids[NUM_HILOS];

        
		imagenRGB=abrirBMP(imagenRecibida,&info);
		displayInfo(&info);
		imagenGray=RGBToGray(imagenRGB,info.width,info.height);
		imagenAux=reservarMemoria(info.width,info.height);
		//filtroPB(imagenGray,imagenAux,info.width,info.height);

		for(i=0;i<NUM_HILOS;i++){
				nhs[i]=i;                                                            //creacion de hilos
				pthread_create(&tids[i],NULL,funHilo,(void *)&nhs[i]);               //crea varios hilos
		}
		for(k=0;k<NUM_HILOS;k++){
				pthread_join(tids[k],(void**)&hilo);                               //espera a que termine la ejecucion del hilo
				printf("\nHilo %d terminado\n",*hilo);
		}
		GraytoRGB(imagenRGB,imagenAux, info.width,info.height);
        
        //crear el nombre de la imagen de resultado con su PID...Nombre unico
        sprintf(str, "%d", someInt);
        strcat(nombreImagen,str);
        strcat(nombreImagen,ext);
        printf("%s",nombreImagen);
				
        guardarBMP(nombreImagen,&info,imagenRGB);
		
		free(imagenRGB); 
		free(imagenGray);
		free(imagenAux);
		//Envia imagen procesada
		printf("Enviando imagen procesada ....");
		send_image(cliente_sockfd, nombreImagen);

        close (cliente_sockfd);
		kill(getppid(),SIGUSR1);  //señal para avisar del termino del proceso
        exit(0);
	  }

	}

	printf("Concluimos la ejecución de la aplicacion Servidor \n");
/*
 *	Cierre de las conexiones
 */

   	close (sockfd);   	
	return 0;
}

void ISRsignal(int sig)// se invoca automaticamente sin enviarle el int
{
    pid_t pidh;
    int estado;

    if(sig==SIGUSR1)
    {
        pidh = wait(&estado); //Termina el proceso hijo
        printf("Señal USR1 recibida en la ISR, del proceso hijo %d terminado con pid %d\n",estado>>8,pidh);
    }
    return;
}


int receive_image(int socket, char nombre[]){ 

	int recv_size = 0,size = 0, read_size, write_size, packet_index =1,stat;

	char imagearray[65500]; //65,507 bytes maximo //10241
	FILE *image;

	//Obtener el tamaño de la imagen
	do{
		stat = read(socket, &size, sizeof(int));
	}while(stat<0);

	printf("Paquete recibido.\n");
	printf("Tamanio de paquete: %i\n",stat);
	printf("Tamaño de imagen: %i\n",size);
	printf(" \n");

	char buffer[] = "Obtenido";

	//Enviar respuesta de recibido
	do{
		stat = write(socket, &buffer, sizeof(int));
	}while(stat<0);

	printf("Respuesta enviada\n");
	printf(" \n");

	//se abre el fichero de la imagen con el nombre especifico con el PID como sufijo
	image = fopen(nombre, "w");

	if( image == NULL) 
	{
		printf("Error has occurred. Image file could not be opened\n");
		return -1; 
	}


	struct timeval timeout = {10,0};

	fd_set fds;					//sockets a comprobar se introducen en el conjunto
	int buffer_fd;

	while(recv_size < size) { //Mientras no recibamos el archivo completo
	
    	FD_ZERO(&fds); // inicializar el contenido del puntero (conjunto)
    	FD_SET(socket,&fds); //Utilizar descriptor y agregar el socket servidor al conjunto

      // select: Nos permite monitorear un conjunto de descriptores de sockets y nos avisa
      // cuales tienen datos para leer, cuáles están listos para escribir,
      // y cuáles producieron excepciones. 

    	buffer_fd = select(FD_SETSIZE,&fds,NULL,NULL,NULL); //&timeout

    	if (buffer_fd < 0)
       		printf("error: en el descriptor de archivo\n");

    	if (buffer_fd == 0)
       		printf("error: tiempo de lectura del buffer expiro\n");

    	if (buffer_fd > 0)
    	{
        	do{
               read_size = read(socket,imagearray, 65500); //10241
            }while(read_size <0);

            printf("Numero de paquete recibido: %i\n",packet_index);
        	printf("Tamaño de paquete: %i\n",read_size);


        	//escribir los datos leidos en el archivo de imagen
        	write_size = fwrite(imagearray,1,read_size, image);
        	printf("Datos escritos en la imagen: %i\n",write_size); 

            if(read_size !=write_size) {
                 printf("Error en la escritura de la imagen\n");    
            }


            //Incrementar el numero total de bytes leidos
            recv_size += read_size;
            packet_index++;
            printf("Tamanio total recibido de la imagen: %i\n",recv_size);
            printf(" \n");
            printf(" \n");
      }

    }
  	fclose(image);
  	printf("Imagen recibida exitosamente!\n");
  	return 1;
}


int send_image(int socket, char nombre[]){

	FILE *picture;
  	int size, read_size, stat, packet_index;
  	char send_buffer[65500], read_buffer[256];
  	packet_index = 1;

  	picture = fopen(nombre, "r");
  	printf("Obteniendo el tamanio de la imagen\n");   

  	if(picture == NULL) {
    	printf("Error al abrir el archivo"); } 

  	fseek(picture, 0, SEEK_END);
  	size = ftell(picture);
  	fseek(picture, 0, SEEK_SET);
  	printf("Tamaño total de la imagen: %i\n",size);

  	//Envia tamanio de la imagen
  	printf("Enviando tamanio de la imagen...\n");
  	write(socket, (void *)&size, sizeof(int));

 	 //Enviar imagen como arreglo de bytes
  	printf("Enviando imagen como arreglo de bytes...\n");

  	do { //Envio de los datos de la imagen
     	stat=read(socket, &read_buffer , 255);
     	printf("Bytes a leer: %i\n",stat);
  	} while (stat < 0);

  	printf("Dato recibido en socket...\n");
  	printf("Datos del socket: %c\n",read_buffer);

  	while(!feof(picture)) {

      	//Leer del archivo al buffer de envio
   		read_size = fread(send_buffer, 1, sizeof(send_buffer)-1, picture);

      	//Enviar datos a traves del socket
   		do{
       		stat = write(socket, send_buffer, read_size);  
  	 	}while (stat < 0);//si no hay nada seguira leyendo hasta que lea imprimira lo siguiente 

   		printf("Paquete numero: %i\n",packet_index);
   		printf("Tamanio de paquete enviado: %i\n",read_size);     
   		printf(" \n");
   		printf(" \n");


   		packet_index++;  //aumenta el indice de los paquetes

      	//Rellena toda la estructura de 0's
        //Es como memset() pero inicializando a 0 todas la variables
      	bzero(send_buffer, sizeof(send_buffer));
  }
}
