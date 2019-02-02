#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> 
#include "defs.h"
#include "procesos.h"
    
void procesoHijo(int np, int pipefd[]){
    extern float seno[MUESTRAS];
    extern float ham[MUESTRAS];
    extern float res[MUESTRAS];
            register int i;
            int tamBloque=MUESTRAS/NUM_PROC;                                               //bloques por hilo
            int iniBloque=np*tamBloque;                                             //inicio del bloque
            int finBloque=iniBloque+tamBloque;  
            printf("\nProceso hijo con pid %d \n",getpid());
            close(pipefd[0]);                                                       //cerramos el canal que no se usa
            for(i=iniBloque;i< finBloque; i++){
                res[i]=ham[i]*seno[i];   
            }
                write(pipefd[1],res+iniBloque ,sizeof(int)*tamBloque);                //se envían C (apuntador) + el inicio del bloque y el tamaño es de int por el tamaño del bloque completo
                close(pipefd[1]);
                exit(np);                  
}
void procesoPadre(int pipefd[NUM_PROC][2]){
    extern float res[MUESTRAS];
            register int np;
            int tamBloque=MUESTRAS/NUM_PROC;                                             //bloques por hilo
            int iniBloque;                                                        //inicio del bloque
            int pid,proc,prc;
            pid=getpid();
            
            for(np=0;np<NUM_PROC;np++){
                close(pipefd[np][1]);
                pid=wait(&proc);
                prc=proc>>8;                                                        //Recibe el numero de proceso
                iniBloque=np*tamBloque; 
                read(pipefd[prc][0],res+iniBloque, sizeof(int)*tamBloque);                 //read recibe los parametros de la tuberia
                printf("\nProceso hijo %d terminado con pid  %d  \n",prc,pid); 
                close(pipefd[prc][0]);  
            }   
            printf("\n");
                  
}