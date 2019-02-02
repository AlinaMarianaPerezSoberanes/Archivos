#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PUERTO 5000
#define TAM_BUFFER 100
#define DIR_IP "192.168.0.136" //"192.168.1.72"
int send_image(int socket);
int receive_image(int socket);
int main(int argc, char **argv)
{
	int tamano_direccion, sockfd;
	struct sockaddr_in direccion_servidor;
	char leer_mensaje[TAM_BUFFER];
/*	
 *	AF_INET - Protocolo de internet IPV4
 *  htons - El ordenamiento de bytes en la red es siempre big-endian, por lo que
 *  en arquitecturas little-endian se deben revertir los bytes
 */	
	memset (&direccion_servidor, 0, sizeof (direccion_servidor));
	direccion_servidor.sin_family = AF_INET;
	direccion_servidor.sin_port = htons(PUERTO);
/*	
 *	inet_pton - Convierte direcciones de texto IPv4 en forma binaria
 */	
	if( inet_pton(AF_INET, DIR_IP, &direccion_servidor.sin_addr) <= 0 ) //inet_pton jace la conversion de la cadena IP a numerico
	{
		perror("Ocurrio un error al momento de asignar la direccion IP");
		exit(1);
	}
/*
 *	Creacion de las estructuras necesarias para el manejo de un socket
 *  SOCK_STREAM - Protocolo orientado a conexión
 */
	printf("Creando Socket ....\n");
	if( (sockfd = socket (AF_INET, SOCK_STREAM, 0)) < 0 )
	{
		perror("Ocurrio un problema en la creacion del socket");
		exit(1);
	}
/*
 *	Inicia el establecimiento de una conexion mediante una apertura
 *	activa con el servidor
 *  connect - ES BLOQUEANTE
 */
	printf ("Estableciendo conexion ...\n");
	if( connect(sockfd, (struct sockaddr *)&direccion_servidor, sizeof(direccion_servidor) ) < 0) 
	{
		perror ("Ocurrio un problema al establecer la conexion");
		exit(1);
	}
/*
 *	Inicia la transferencia de datos entre cliente y servidor
 */
	send_image(sockfd);
  printf("Recibiendo Imagen procesada");
  receive_image(sockfd);
	
	printf ("Cerrando la aplicacion cliente\n");
/*
 *	Cierre de la conexion
 */
	close(sockfd);

	return 0;
}


int send_image(int socket){

  FILE *picture;
    int size, read_size, stat, packet_index;
    char send_buffer[65500], read_buffer[256];
    packet_index = 1;

    picture = fopen("hoja.bmp", "r");
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

int receive_image(int socket){ 

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
  image = fopen("imagenProcesada.bmp", "w");

  if( image == NULL) 
  {
    printf("Error has occurred. Image file could not be opened\n");
    return -1; 
  }


  struct timeval timeout = {10,0};

  fd_set fds;         //sockets a comprobar se introducen en el conjunto
  int buffer_fd;

  while(recv_size < size) { //Mientras no recibamos el archivo completo
  
      FD_ZERO(&fds); // inicializar el contenido del puntero (conjunto)
      FD_SET(socket,&fds); //Utilizar descriptor y agregar el socket servidor al conjunto

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


	
