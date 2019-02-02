#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include "defs.h"
#include "hilos.h"
extern float seno[MUESTRAS];
extern float ham[MUESTRAS];
extern float res[MUESTRAS];

void * funHilo(void *arg){
    register int i=0;
    int nh=*(int*)arg;        
        for( i=nh ; i<MUESTRAS; i+=NUM_HILOS ){
            res[i]=ham[i]*seno[i];
        }
    pthread_exit(arg);
}