#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>   
#include "defs.h"
#include "proc.h"                                                                //Para tuberia 
                                        
extern int *A,*B;
extern int pp;

void procesoHijo(int np, int pipefd[]){
            register int i;
            printf("\nProceso hijo con pid %d \n",getpid());
            close(pipefd[0]); 
            pp=0;                                                            //cerramos el canal que no se usa
            for(i=np;i< N; i+=NUM_PROC){
                pp+=A[i]*B[i];   
            }
                write(pipefd[1],&pp,sizeof(int));                           //se envían C (apuntador) + el inicio del bloque y el tamaño es de int por el tamaño del bloque completo
                close(pipefd[1]);
                exit(np);                  
}
void procesoPadre(int pipefd[]){
            register int np;
            int pid,proc,prc,suma_parcial;
            pid=getpid();
             close(pipefd[1]);
            for(np=0;np<NUM_PROC;np++){
               
                pid=wait(&proc);
                prc=proc>>8;                                                        //Recibe el numero de proceso
                read(pipefd[0],&suma_parcial, sizeof(int));
                pp+=suma_parcial;                           //read recibe los parametros de la tuberia
                printf("\nProceso hijo %d terminado con pid  %d  \n",prc,pid);      
            }
            close(pipefd[0]);    
            printf("\n");
                  
}

void imprimir(int *datos){
    register int n;
    for(n=0;n<N;n++){
        if(!(n%16)){ 
            printf("\n");
        }
        printf("%4.d ",datos[n]);
    }
    printf("\n");
}

void llenarArreglo(int *datos){
    register int n;
    for(n=0;n<N;n++){
        datos[n]= rand() % 256;
    }
}

int *reservarMemoria(void){
    int *mem;
    mem=(int *)malloc(sizeof(int)*N);
    if(!mem){
        perror("Error al signar memoria");
        exit(EXIT_FAILURE);
    }else{
        return mem;
    }
}