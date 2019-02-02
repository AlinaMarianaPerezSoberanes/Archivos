//Ordenar arreglo 
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>       //Para tuberia 
#include <string.h>
#define N 64
#define NUM_PROC 4
int *reservarMemoria(void);
void llenarArreglo(int *datos);
void imprimir(int *datos);
int mayorArreglo(int *datos);
int menorArreglo(int *datos);
void procesoHijo(int np, int *datos, int pipefd[]);
void procesoPadre(int pipefd[]);
int promediaArreglo(int *datos);
int *ordenarArreglo(int *datos);

int main(){
    int pipefd[2];                                  //Crea dos elementos para la tubería 
    int edo;
    pid_t pid;
    register int np;
    int *datos;
    datos= reservarMemoria();
    llenarArreglo(datos);
    imprimir(datos);
    fflush(stdout);
    /*Creacion de pipe*/
    edo=pipe(pipefd);
    if(edo==-1){
        perror("Error al crear al pipe");
        exit(EXIT_FAILURE);
    }

        for(int np=0;np<NUM_PROC;np++){
            pid=fork();
            if(!pid){                                   //Proceso hijo
                procesoHijo(np,datos,pipefd);
            }
        }
        procesoPadre(pipefd);                         //Proceso padre 
      
}
void procesoPadre(int pipefd[]){
            register int np;
            int pid,resultado,proc,prc;
            int *aux;
            aux = (int *) malloc ((sizeof(int) * N));
            pid=getpid();
            close(pipefd[1]);
            for(np=0;np<NUM_PROC;np++){
                pid=wait(&proc);
                prc=proc>>8;                              //Recibe el numero de proceso
                if(prc==3){
                    read(pipefd[0],aux,sizeof(int)*N);      //read recibe los parametros de la tuberia                    //imprimir(aux);                    
                    imprimir(aux);
                }
                else{   
                    read(pipefd[0],&resultado, sizeof(int));      //read recibe los parametros de la tuberia
                    printf("\nProceso hijo %d terminado con pid  %d con el resultado %d \n",proc>>8,pid,resultado);
                }
                
            }   
            printf("\n");
            close(pipefd[0]);
            free(aux);        
}

void procesoHijo(int np, int *datos, int pipefd[]){
    int mayor,menor, promedio;
    int *aux;
            //pid=getpid();
            printf("\nProceso hijo con pid %d \n",getpid());
            close(pipefd[0]);                           //cerramos el canal que no se usa
            if(np==0){
               mayor= mayorArreglo(datos);
               write(pipefd[1],&mayor,sizeof(int));     //Se escribe en el 1
               close(pipefd[1]);
               exit(np);
            }if(np==1){
                menor= menorArreglo(datos);
                write(pipefd[1],&menor,sizeof(int));     //Se escribe en el 1
                close(pipefd[1]);                        //Liberamos el descriptor que ya no se usa
                exit(np);
            }
            if(np==2){
                promedio= promediaArreglo(datos);
                write(pipefd[1],&promedio,sizeof(int));     //Se escribe en el 1
                close(pipefd[1]);                        //Liberamos el descriptor que ya no se usa
                exit(np);
            }
            if(np==3){
                aux=ordenarArreglo(datos);
                write(pipefd[1],aux,sizeof(int)*N);     //Se escribe en el 1
                close(pipefd[1]);                      //Liberamos el descriptor que ya no se usa
                exit(np);
            }
                     
}

int *ordenarArreglo(int *datos){
    register int i,j,n;
    int aux;
    for(i=0; i < N-1; i++){
        for(j=0; j < N-1; j++){
            if(datos[j] > datos[j+1]){
                aux=datos[j];
                datos[j]=datos[j+1];
                datos[j+1]=aux;
            }
        }
    } 
    return datos;
}

int promediaArreglo(int *datos){
    int suma=0;
    register int n;
    for(n=0;n<N;n++){
        suma=suma+datos[n];
    }
    //printf("SUMA: %d \n",suma);
    //printf("prom: %d \n",suma>>6);
 return suma>>6;
}

int menorArreglo(int *datos){
     register int n;
     int menor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]<menor){
                menor=datos[n];
        }
    }
    return menor;
}

int mayorArreglo(int *datos){
     register int n;
     int mayor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]>mayor){
                mayor=datos[n];
        }
    }
    return mayor;
}

void imprimir(int *datos){
    register int n;
    for(n=0;n<N;n++){
        if(!(n%16)){ 
            printf("\n");
        }
        printf("%4.d ",datos[n]);
    }
}

void llenarArreglo(int *datos){
    register int n;
    for(n=0;n<N;n++){
        datos[n]= rand() % 4096;
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