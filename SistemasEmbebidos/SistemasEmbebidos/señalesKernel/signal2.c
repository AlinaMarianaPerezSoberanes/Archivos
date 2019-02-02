/*PROGRAMA CON ARCHIVOS*/
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#define NUM_PROC 4
void procesoPadre(int pid[]);
void procesoHijo(int np);
void ISRsignal(int sig);
int main(){
    register int i;
    pid_t pid[NUM_PROC];
    int estado;
    printf("Probando procesos ... \n");
    if(signal(SIGUSR1,ISRsignal)==SIG_ERR){                                     // no termina el proceso
        perror("Error al crear la señal\n");
        exit(EXIT_FAILURE);
    }
    for(i=0;i<NUM_PROC;i++){
        pid[i]=fork();
         if(pid[i]==0){
            
            procesoHijo(i);  
         }
    }
    procesoPadre(pid);
    return 0;
}

void ISRsignal(int sig){
    if(sig==SIGUSR1){
        printf("Señal USR1 recibida en la ISR \n");
    }
}

void procesoPadre(int pid[]){
            register int np;
            int estado;
            pid_t p;

            printf("Proceso padre con pid %d \n",getpid());
            sleep(10);
            for(np=0;np<NUM_PROC;np++){
                kill(pid[np],SIGUSR1);
            }
            for(np=0;np<NUM_PROC;np++){
                p=wait(&estado);
                printf("Proceso hijo %d terminado con pid %d \n",estado>>8,p);
            }          
}

void procesoHijo(int np){
            printf("Proceso hijo %d con pid %d \n",np,getpid());
            pause();
            printf("Señal recibida en el proceso hijo");
            exit(np);
}