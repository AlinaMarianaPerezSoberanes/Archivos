#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>

int main(){
    float suma,resta, n1=56, n2=23;
    pid_t pid;
    int estado;
    pid=fork();
    
    if(pid==0){
        pid=getpid();
        printf("Proceso hijo con pid %d \n",getpid());
        suma=n1+n2;
        printf("Suma= %f \n",suma);
        exit(0);
    }else{
        pid=getpid();
         printf("Proceso padre con pid %d \n",getpid());
         resta=n1-n2;
         printf("resta= %f \n",resta);
         pid=wait(&estado);
         //wait(&estado);
    }
    
    return 0;
}