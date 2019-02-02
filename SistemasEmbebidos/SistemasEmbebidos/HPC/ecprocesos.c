//funcion sinoidal discreta y hamming con hilos y con procesos para el viernes
//usar externs para las variables globales en otros codigos, no en eñ .h
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>                                                                   //Para tuberia 
#define N 64
#define NUM_PROC 4

void * funHilo(void *arg);   
int *reservarMemoria(void);
void llenarArreglo(int *datos);
void imprimir(int *datos);
void procesoHijo(int np, int pipefd[]);
void procesoPadre(int pipefd[]);                                           
int *A;
int promedio;

int main(){
    int pipefd[2];                                                         //Crea dos elementos para la tubería 
    int edo;
    pid_t pid;
    A=reservarMemoria();                                                            //reservamos memoria a los arreglos
    //srand(time(NULL));
    llenarArreglo(A);                                                               //llenamos lo arreglos con datos
    imprimir(A);   
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
    printf("Promedio es %d:",promedio);
    free(A);
    return 0;
}
void procesoHijo(int np, int pipefd[]){
            register int i;
            printf("\nProceso hijo con pid %d \n",getpid());
            close(pipefd[0]); 
            promedio=0;                                                            //cerramos el canal que no se usa
            for(i=np;i< N; i+=NUM_PROC){
                promedio+=A[i];   
            }
                write(pipefd[1],&promedio,sizeof(int));                           //se envían C (apuntador) + el inicio del bloque y el tamaño es de int por el tamaño del bloque completo
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
                promedio+=suma_parcial;                           //read recibe los parametros de la tuberia
                printf("\nProceso hijo %d terminado con pid  %d  \n",prc,pid);      
            }
            promedio/=N;
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