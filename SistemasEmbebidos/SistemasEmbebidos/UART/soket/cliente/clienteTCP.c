#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PUERTO 5000
#define TAM_BUFFER 100
#define DIR_IP "127.0.0.1" //"192.168.1.72"

int receive_arch(int socket);
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
  printf("Recibiendo ubicación del servidor");
  receive_arch(sockfd);
	
	printf ("Cerrando la aplicacion cliente\n");
/*
 *	Cierre de la conexion
 */
	close(sockfd);

	return 0;
}

int receive_arch(int socket){ 

  int recv_size = 0,size = 0, read_size, write_size, packet_index =1,stat;

  char array[65500]; //65,507 bytes maximo //10241
  FILE *archivo;

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
  archivo = fopen("ubicacion.txt", "w");

  if( archivo == NULL) 
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
               read_size = read(socket,array, 65500); //10241
            }while(read_size <0);

            printf("Numero de paquete recibido: %i\n",packet_index);
          printf("Tamaño de paquete: %i\n",read_size);


          //escribir los datos leidos en el archivo de imagen
          write_size = fwrite(array,1,read_size, archivo);
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
    fclose(archivo);
    printf("Archivo recibido exitosamente!\n");
    return 1;
}


	
