#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include "defs.h"
#include "hilo.h"
                                            
int *A,*B;
int pp;
pthread_mutex_t bloqueo;

int main(){
    int *hilo,i,k,nhs[NUM_HILOS];
    pthread_t tids[NUM_HILOS];
    A=reservarMemoria();                                                    //reservamos memoria a los arreglos
    B=reservarMemoria();
    llenarArreglo(A);                                                       //llenamos lo arreglos con datos
    llenarArreglo(B);
    imprimir(A);
    imprimir(B);
    pthread_mutex_init(&bloqueo,NULL);
    for(i=0;i<NUM_HILOS;i++){
        nhs[i]=i;                                                           //creacion de hilos
        pthread_create(&tids[i],NULL,funHilo,(void *)&nhs[i]);              //crea varios hilos
    }
    for(k=0;k<NUM_HILOS;k++){
         pthread_join(tids[k],(void**)&hilo);                               //espera a que termine la ejecucion del hilo
         printf("\nHilo %d terminado\n",*hilo);
    }
    printf("El producto punto es: %d\n",pp);
     pthread_mutex_destroy(&bloqueo);
    free(A);
    free(B);
    return 0;
}