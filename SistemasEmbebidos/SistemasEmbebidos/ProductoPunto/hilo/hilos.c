#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include "defs.h"
#include "hilo.h"
extern int *A,*B;
extern int pp;
extern pthread_mutex_t bloqueo;

//  FUNCION DE FORMA PARALELA
void * funHilo(void *arg){
    register int i=0;
    int nh=*(int*)arg;
    int suma_parcial=0;    
        for( i=nh ; i<N ; i+=NUM_HILOS ){
            suma_parcial+=A[i]*B[i];
        }
        pthread_mutex_lock(&bloqueo);
        pp+=suma_parcial;
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
