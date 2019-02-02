#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>

int main(){
    register float suma,resta, n1=56, n2=23;
    pid_t pid;
    int estado;
    pid=fork();
    
    for(int i=0;i<8;i++){
         if(pid==0){
            
            procesoHijo(pid);
           
        }else{
            procesoPadre();
            pid=wait(&estado);
        }
    }
    return 0;
}
void procesoPadre(){
            register int np;
            int pid,estado;
            pid=getpid();
            //printf("Proceso padre con pid %d \n",getpid());
            //resta=n1-n2;
            printf("resta= %f \n",resta);
            for(np=0; np<; np++){
                pid=wait(&estado);
                printf("Proceso hijo terminado %d",pid);
            }
            
}

void procesoHijo(int np){
            pid=getpid();
            printf("Proceso hijo con pid %d \n",getpid());
            //suma=n1+n2;
            //printf("Suma= %f \n",suma);
            exit(np);
}