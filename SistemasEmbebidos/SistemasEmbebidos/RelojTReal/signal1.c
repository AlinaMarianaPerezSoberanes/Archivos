/*kill -SIGINT 3582
kill -SIGTERM 3582
KILL -SIGKILL es una señal definitiva
*/
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
void ISRsignal(int sig);
int main(){
    if(signal(SIGALRM,ISRsignal)==SIG_ERR){                                     // no termina el proceso
        perror("Error al crear la ISR\n");
        exit(EXIT_FAILURE);
    }
    if(signal(SIGINT,ISRsignal)==SIG_ERR){                                     // no termina el proceso
        perror("Error al crear la ISR\n");
        exit(EXIT_FAILURE);
    }
    if(signal(SIGTERM,ISRsignal)==SIG_ERR){                                     //detiene el proceso
        perror("Error al crear la ISR\n");
        exit(EXIT_FAILURE);
    }
    alarm(5);
    while(1)
        pause();
}

void ISRsignal(int sig){
    static int cont=0;
    if(sig==SIGINT){
        printf("No quiero terminar ... \n");
    }else if(sig==SIGTERM){
        printf("No entiendes, no quiero terminar ...\n");
    }
    else if(sig==SIGALRM){
        ;
        printf("Temporizador ejecutando ...\n");
        cont++;
        if(cont==10)
            alarm(0);
        else
            alarm(5);
    }
}
