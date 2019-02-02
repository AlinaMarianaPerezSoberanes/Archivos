#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <pthread.h>
#include"defs.h"
#include"procesamiento.h"
#include "archivos.h"
#include "hilos.h"
    float seno[MUESTRAS];
	float ham[MUESTRAS];
	float res[MUESTRAS];
int main(){
	int *hilo,i,k,nhs[NUM_HILOS];
    pthread_t tids[NUM_HILOS];
	genera_seno(seno);
	genera_ham(ham);
    for(i=0;i<NUM_HILOS;i++){
        nhs[i]=i;                                                           //creacion de hilos
        pthread_create(&tids[i],NULL,funHilo,(void *)&nhs[i]);              //crea varios hilos
    }
    for(k=0;k<NUM_HILOS;k++){
         pthread_join(tids[k],(void**)&hilo);                               //espera a que termine la ejecucion del hilo
         printf("\nHilo %d terminado\n",*hilo);
    }
	guarda_datos(seno,ham,res);
    return 0;
}
