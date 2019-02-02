#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>                                                                   //Para tuberia 
#include "defs.h"
#include "proc.h" 
                                           
int *A,*B;
int pp;

int main(){
    int pipefd[2];                                                                  //Crea dos elementos para la tubería 
    int edo;
    pid_t pid;
    A=reservarMemoria();                                                            //reservamos memoria a los arreglos
    B=reservarMemoria();
    //srand(time(NULL));
    llenarArreglo(A);                                                               //llenamos lo arreglos con datos
    llenarArreglo(B);
    imprimir(A);   
    imprimir(B);
    edo =pipe(pipefd); 
    if(edo==-1){
        perror("Error al crear al pipe");
        exit(EXIT_FAILURE);
    }
        for(int np=0;np<NUM_PROC;np++){
            pid=fork();
            if(!pid){                                                               //Proceso hijo
                procesoHijo(np,pipefd);
            }
        }
    procesoPadre(pipefd);  
    printf("El producto punto es %d:",pp);
    free(A);
    free(B);
    return 0;
}