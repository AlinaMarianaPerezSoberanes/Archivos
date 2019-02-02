/** @brief: Este programa muestra el uso del UART
 * investigar formato de las cadenas del modulo para extraer la ubicación
*/

#include <stdio.h>
#include <stdlib.h>
#include <termios.h>													//archivos definidos 
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

#define N  1024
#define T  80

int config_serial ( char *, speed_t );
int reconocimiento(char dato[T]);

int main()
{
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
		printf("%c", dato);/*
		arr[cont]=dato;
		cont++;
		if(dato=='\n'){
			//printf("Yes");
			re=reconocimiento(arr);
			cont=0;
			if(re==1){
				break;
			}
		}	*/		
	}
	printf("Tenemos datos");

	close( fd_serie );

	return 0;
}

/** @brief: Esta funcion Configura la interfaz serie
 *  @param: dispositivo_serial, Nombre el dispositivo serial a usar: ttyUSB0, ttyUSB1, etc
 *  @param: baudios, Velocidad de comunicacion. Se usa la constante Bxxxx, donde xxxx  es la
 *          velocidad. Estan definidas en termios.h. Ejemplo: B9600, B19200..
 *  @return: fd, Descriptor del serial
 *******************************************************************************************
 */
int config_serial( char *dispositivo_serial, speed_t baudios )
{
	struct termios newtermios;
  	int fd;
/*
 * Se abre un descriptor de archivo para manejar la interfaz serie
 * O_RDWR - Se abre el descriptor para lectura y escritura
 * O_NOCTTY - El dispositivo terminal no se convertira en el terminal del proceso
 * ~O_NONBLOCK - Se hace bloqueante la lectura de datos
 */
  	fd = open( dispositivo_serial, (O_RDWR | O_NOCTTY) & ~O_NONBLOCK );
	if( fd == -1 )
	{
		printf("Error al abrir el dispositivo tty \n");
		exit( EXIT_FAILURE );
  	}
/*
 * cflag - Proporciona los indicadores de modo de control
 *	CBAUD	- Velocidad de transmision en baudios.
 * 	CS8	- Especifica los bits por dato, en este caso 8
 * 	CLOCAL 	- Ignora las lineas de control del modem: CTS y RTS
 * 	CREAD  	- Habilita el receptor del UART
 * iflag - proporciona los indicadores de modo de entrada
 * 	IGNPAR 	- Ingnora errores de paridad, es decir, comunicación sin paridad
 * oflag - Proporciona los indicadores de modo de salida
 * lflag - Proporciona indicadores de modo local
 * 	TCIOFLUSH - Elimina datos recibidos pero no leidos, como los escritos pero no transmitidos
 * 	~ICANON - Establece modo no canonico, en este modo la entrada esta disponible inmediatamente
 * cc[]	 - Arreglo que define caracteres especiales de control
 *	VMIN > 0, VTIME = 0 - Bloquea la lectura hasta que el numero de bytes (1) esta disponible
 */
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
/*
 * Se establece los parametros de terminal asociados con el
 * descriptor de archivo fd utilizando la estructura termios
 * TCSANOW - Cambia los valores inmediatamente
 */
	if( tcsetattr( fd, TCSANOW, &newtermios ) == -1 )
	{
		printf("Error al establecer los parametros de la terminal \n" );
		exit( EXIT_FAILURE );
	}
//Retorna el descriptor de archivo
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


