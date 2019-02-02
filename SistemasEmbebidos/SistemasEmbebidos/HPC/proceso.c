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
void procesoPadre(int pipefd[NUM_PROC][2]);                                           
int *A,*B,*C;

int main(){
    int pipefd[NUM_PROC][2];                                                         //Crea dos elementos para la tubería 
    int edo;
    pid_t pid;
    A=reservarMemoria();                                                            //reservamos memoria a los arreglos
    B=reservarMemoria();
    C=reservarMemoria();
    //srand(time(NULL));
    llenarArreglo(A);                                                               //llenamos lo arreglos con datos
    llenarArreglo(B);

    imprimir(A);
    imprimir(B);

    
    if(edo==-1){
        perror("Error al crear al pipe");
        exit(EXIT_FAILURE);
    }

        for(int np=0;np<NUM_PROC;np++){
            edo =pipe(&pipefd[np][0]);
            pid=fork();
            if(!pid){                                                               //Proceso hijo
                procesoHijo(np,&pipefd[np][0]);
            }
        }
    procesoPadre(pipefd);  
    imprimir(C);
    free(A);
    free(B);
    free(C);
    return 0;
}
void procesoHijo(int np, int pipefd[]){
            register int i;
            int tamBloque=N/NUM_PROC;                                               //bloques por hilo
            int iniBloque=np*tamBloque;                                             //inicio del bloque
            int finBloque=iniBloque+tamBloque;  
            printf("\nProceso hijo con pid %d \n",getpid());
            close(pipefd[0]);                                                       //cerramos el canal que no se usa
            for(i=iniBloque;i< finBloque; i++){
                C[i]=A[i]*B[i];   
            }
                write(pipefd[1],C+iniBloque ,sizeof(int)*tamBloque);                //se envían C (apuntador) + el inicio del bloque y el tamaño es de int por el tamaño del bloque completo
                close(pipefd[1]);
                exit(np);                  
}
void procesoPadre(int pipefd[NUM_PROC][2]){
            register int np;
            int tamBloque=N/NUM_PROC;                                             //bloques por hilo
            int iniBloque;                                                        //inicio del bloque
            int finBloque=iniBloque+tamBloque; 
            int pid,proc,prc;
            pid=getpid();
            
            for(np=0;np<NUM_PROC;np++){
                close(pipefd[np][1]);
                pid=wait(&proc);
                prc=proc>>8;                                                        //Recibe el numero de proceso
                iniBloque=np*tamBloque; 
                read(pipefd[prc][0],C+iniBloque, sizeof(int)*tamBloque);                 //read recibe los parametros de la tuberia
                printf("\nProceso hijo %d terminado con pid  %d  \n",prc,pid); 
                close(pipefd[prc][0]);  
            }   
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