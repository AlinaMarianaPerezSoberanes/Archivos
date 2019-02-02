#include<stdio.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<unistd.h>
#include<stdlib.h>
#define NUM_PROC 4

void ISRsignal(int sig);
void proceso_hijo( int np );
void proceso_padre( int pid[]);

int s;

int main()
{
    register int np;
    pid_t pid[NUM_PROC];
    //int status;


    if(signal(SIGUSR1, ISRsignal)==SIG_ERR) //señal de usuario 
    {
        perror("Error al crear la señal\n");
        exit(EXIT_FAILURE);
    }

    for( np = 0; np < NUM_PROC; np++ )
    {
        pid[np] = fork();//varios procesos, pids
        if( pid[np] == -1 )
        {
            perror("Error al generar el proceso");
            exit(EXIT_FAILURE);
        }else if( !pid[np] )
        {
            proceso_hijo( np );
        }
    }
    proceso_padre(pid); //se le envian los pid
 
    return 0;
}

void ISRsignal(int sig)// se invoca automaticamente sin enviarle el int
{
   
    if(sig==SIGUSR1)
    {
        printf("\nSeñal USR1 recibida en la ISR");
        s=1;
    }
    return;
}
// void ISRsignal(int sig)// se invoca automaticamente sin enviarle el int
// {
//     pid_t pidh;
//     int estado;

//     if(sig==SIGUSR1)
//     {
//         pidh = wait(&estado);
//         printf("Señal USR1 recibida en la ISR, del proceso hijo %d terminado con pid %d\n",estado>>8,pidh);
//     }
//     return;
// }


void proceso_hijo( int np )
{
    printf("Proceso hijo %d con pid %d \n", np, getpid());
    kill(getppid(),SIGUSR1); // getppid el identificador del proceso al cual deseamos enviar la señal 
    exit(np);
}
 
void proceso_padre(int pid[])
{
    pid_t pidh;
    int estado;
    s=0;
 	printf("Proceso padre con pid %d \n", getpid());
    sleep(10);
    pause();
    while(s==1)
    {
        pause();
        pidh = wait(&estado);
        printf("\nSeñal USR1 recibida en la ISR, del proceso hijo %d terminado con pid %d\n",estado>>8,pidh);
        s=0;
    }

}


// void ISRsignal(int sig)// se invoca automaticamente sin enviarle el int
// { 
//     if(sig==SIGUSR1)
//     {
//         printf("Señal USR1 recibida en la ISR del proceso hijo con pid %d\n",getpid());
//     }
// }