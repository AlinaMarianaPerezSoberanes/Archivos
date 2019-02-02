#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <termios.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

#define PUERTO 			5000	//Número de puerto asignado al servidor
#define COLA_CLIENTES 	5 		//Tamaño de la cola de espera para clientes
#define TAM_BUFFER 		100
#define N  1024
#define T  80

int send_arch(int socket);		//Enviar archivo
void ISRsignal(int sig); 		//señal de usuario 
void * funHilo(void *arg);		//peticiones del UART
int config_serial ( char *, speed_t ); //configuracion del UART
int reconocimiento(char dato[T]);	//Reconocimiento de ubicacion


int main(int argc, char **argv){
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
		int hilo;
		pthread_t tid_s;
   		pthread_create(&tid_s,NULL,funHilo,NULL);		//Creamos hilo
		pthread_join(tid_s,(void**)&hilo);				//Espera que el hilo finalice
		
		//Envia imagen procesada
		printf("Enviando archivo ....");
		send_arch(cliente_sockfd);						//Enviamos archivo creado con la ubiacion

        close (cliente_sockfd);
		kill(getppid(),SIGUSR1);  						//señal para avisar del termino del proceso
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


void * funHilo(void *arg){
    register int i;
	int fd_serie;
	char dato;
	char arr[T];
	int cont=0;
	int re;

	fd_serie = config_serial( "/dev/ttyACM0", B9600 ); 					//descriptor del archivo, velocidad de baudios
	printf("serial abierto con descriptor: %d\n", fd_serie);
	//dato=reservarMemoria();
	//Leemos N datos del UART
	for( ;1; )
	{
		read ( fd_serie, &dato, 1 );
		//printf("%c", dato);
		arr[cont]=dato;
		cont++;
		if(dato=='\n'){
			//printf("Yes");
			re=reconocimiento(arr);
			cont=0;
			if(re==1){
				break;
			}
		}			
	}
	printf("Tenemos datos");

	close( fd_serie );
        
    pthread_exit(arg);
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

int send_arch(int socket){

	FILE *archivo;
  	int size, read_size, stat, packet_index;
  	char send_buffer[65500], read_buffer[256];
  	packet_index = 1;

  	archivo = fopen("ubicacion.txt", "r");
  	printf("Obteniendo el tamanio del archivo\n");   

  	if(archivo == NULL) {
    	printf("Error al abrir el archivo"); } 

  	fseek(archivo, 0, SEEK_END);
  	size = ftell(archivo);
  	fseek(archivo, 0, SEEK_SET);
  	printf("Tamaño total del archivo: %i\n",size);

  	//Envia tamanio de la imagen
  	printf("Enviando tamanio del archivo...\n");
  	write(socket, (void *)&size, sizeof(int));

 	 //Enviar imagen como arreglo de bytes
  	printf("Enviando imagen como arreglo de bytes...\n");

  	do { //Envio de los datos de la imagen
     	stat=read(socket, &read_buffer , 255);
     	printf("Bytes a leer: %i\n",stat);
  	} while (stat < 0);

  	printf("Dato recibido en socket...\n");
  	printf("Datos del socket: %c\n",read_buffer);

  	while(!feof(archivo)) {

      	//Leer del archivo al buffer de envio
   		read_size = fread(send_buffer, 1, sizeof(send_buffer)-1, archivo);

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

int config_serial( char *dispositivo_serial, speed_t baudios ){
	struct termios newtermios;
  	int fd;
  	fd = open( dispositivo_serial, (O_RDWR | O_NOCTTY) & ~O_NONBLOCK );
	if( fd == -1 )
	{
		printf("Error al abrir el dispositivo tty \n");
		exit( EXIT_FAILURE );
  	}
	newtermios.c_cflag 	= CBAUD | CS8 | CLOCAL | CREAD;
  	newtermios.c_iflag 	= IGNPAR;
  	newtermios.c_oflag	= 0;
  	newtermios.c_lflag 	= TCIOFLUSH | ~ICANON;
  	newtermios.c_cc[VMIN]	= 1;
  	newtermios.c_cc[VTIME]	= 0;

// Configura la velocidad de salida del UART
  	if( cfsetospeed( &newtermios, baudios ) == -1 )
	{
		printf("Error al establecer velocidad de salida \n");
		exit( EXIT_FAILURE );
  	}
// Configura la velocidad de entrada del UART
	if( cfsetispeed( &newtermios, baudios ) == -1 )
	{
		printf("Error al establecer velocidad de entrada \n" );
		exit( EXIT_FAILURE );
	}
// Limpia el buffer de entrada
	if( tcflush( fd, TCIFLUSH ) == -1 )
	{
		printf("Error al limpiar el buffer de entrada \n" );
		exit( EXIT_FAILURE );
	}
// Limpia el buffer de salida
	if( tcflush( fd, TCOFLUSH ) == -1 )
	{
		printf("Error al limpiar el buffer de salida \n" );
		exit( EXIT_FAILURE );
	}
	if( tcsetattr( fd, TCSANOW, &newtermios ) == -1 )
	{
		printf("Error al establecer los parametros de la terminal \n" );
		exit( EXIT_FAILURE );
	}
	return fd;
}

int reconocimiento(char dato[T]){
	// ejemplo de cadena $GPGGA,033124.00,1926.46066,N,09906.95980,W,1,04,4.23,2224.8,M,-7.5,M,,*6C
	FILE *archivo;
	archivo = fopen ( "ubicacion.txt", "w" );        
	if (archivo==NULL) {
		fputs ("File error",stderr); 
		exit (1);
	}
	for(int i=0; i<T;i++){
		printf("%c",dato[i]);
	}printf("\n");
	char latitude[10];
	char indNS;
	int cont=0;
	char longitude[10];
	char indEW;
	if(dato[4]==71 && dato[5]==65){
		if(dato[17]!=44){
			for(int i=17;i<27;i++){
			latitude[cont]=dato[i];
			printf("%c",latitude[cont]);
			cont++;
			}
			indNS=dato[28];
			printf("\n %c \n ",indNS);
			cont=0;
			for(int i=31;i<42;i++){
				longitude[cont]=dato[i];
				printf("%c",longitude[cont]);
				cont++;
			}
			indEW=dato[42];
			printf("\n %c \n ",indEW);
			//Escribir en archivo los datos obtenidos
			fprintf(archivo, "Latitud: ");
			fputs(latitude, archivo);
			fprintf(archivo,"\nIndicador Norte/Sur: %c" ,indNS);
			fprintf(archivo, "\nLongitud: ");
			fputs(longitude, archivo); 
			fprintf(archivo,"\nIndicador Este/Oeste: %c" ,indEW);
			fclose(archivo);
			return 1;
		}
		return 0;
	}
	return 0;
}


