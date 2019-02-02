#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> 
#include"defs.h"
#include"procesamiento.h"
#include "archivos.h"
#include "procesos.h"
float seno[MUESTRAS];
float ham[MUESTRAS];
float res[MUESTRAS];

int main(){
	int pipefd[NUM_PROC][2];                                                         //Crea dos elementos para la tubería 
    int edo=0;
    pid_t pid;
	genera_seno(seno);
	genera_ham(ham);
        for(int np=0;np<NUM_PROC;np++){
            edo =pipe(&pipefd[np][0]);
            pid=fork();
            if(!pid){                                                               //Proceso hijo
                procesoHijo(np,&pipefd[np][0]);
            }
        }
    procesoPadre(pipefd);  
	guarda_datos(seno,ham,res);
    return 0;
}
