#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define N 64
#define NUM_HILOS 4

void * funHilo(void *arg);   
int *reservarMemoria(void);
void llenarArreglo(int *datos);
void imprimir(int *datos);                                             
int *A;
int promedio;
pthread_mutex_t bloqueo;

int main(){
    int *hilo,i,k,nhs[NUM_HILOS];
    pthread_t tids[NUM_HILOS];
    A=reservarMemoria();                                                    //reservamos memoria a los arreglos
    llenarArreglo(A);                                                       //llenamos lo arreglos con datos
    imprimir(A);
    pthread_mutex_init(&bloqueo,NULL);
    for(i=0;i<NUM_HILOS;i++){
        nhs[i]=i;                                                           //creacion de hilos
        pthread_create(&tids[i],NULL,funHilo,(void *)&nhs[i]);              //crea varios hilos
    }
    for(k=0;k<NUM_HILOS;k++){
         pthread_join(tids[k],(void**)&hilo);                               //espera a que termine la ejecucion del hilo
         printf("\nHilo %d terminado\n",*hilo);
    }
    promedio/=N;
    printf("Promedio es: %d\n",promedio);
     pthread_mutex_destroy(&bloqueo);
    free(A);
    return 0;
}
/*  FUNCION POR BLOQUES 
void * funHilo(void *arg){
    register int i=0;
    int nh=*(int*)arg;
    int tamBloque=N/NUM_HILOS;                                                 //bloques por hilo
    int iniBloque=nh*tamBloque;                                                //inicio del bloque
    int finBloque=iniBloque+tamBloque;                                         //fin del bloque
        
        for(i=iniBloque;i<finBloque;i++){
            C[i] = A[i] * B[i];
        }
    pthread_exit(arg);
}*/
//  FUNCION DE FORMA PARALELA
void * funHilo(void *arg){
    register int i=0;
    int nh=*(int*)arg;
    int suma_parcial=0;    
        for( i=nh ; i<N ; i+=NUM_HILOS ){
            suma_parcial+=A[i];
        }
        pthread_mutex_lock(&bloqueo);
        promedio+=suma_parcial;
        pthread_mutex_unlock(&bloqueo);
    pthread_exit(arg);
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