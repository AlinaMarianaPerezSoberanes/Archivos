
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define N 64

int *reservarMemoria(void);
void llenarArreglo(int *datos);                                     //se convierten en hilos
void imprimir(int *datos);

void *mayorArreglo(void *arg);
void *menorArreglo(void *arg);

int main(){
    int *res_mayor,*res_menor;
    pthread_t tid_mayor,tid_menor;
    int *datos;
    datos= reservarMemoria();
    llenarArreglo(datos);
    imprimir(datos);
   
    pthread_create(&tid_mayor,NULL,mayorArreglo,(void*)datos);        //crea el nuevo hilo
    pthread_create(&tid_menor,NULL,menorArreglo,(void*)datos);        //crea el nuevo hilo
   
    pthread_join(tid_mayor,(void**)&res_mayor);                       //espera a que termine la ejecucion del hilo
    pthread_join(tid_menor,(void**)&res_menor);

    printf("\nEl mayor es: %d\n",*res_mayor);
    printf("\nEl menor es: %d\n",*res_menor);

    return 0;
}

void * menorArreglo(void *arg){
     register int n;
     int *datos=(int*)arg;
     static int menor;
     menor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]<menor){
                menor=datos[n];
        }
    }
    pthread_exit((void*)&menor);
}

void * mayorArreglo(void *arg){
     register int n;
     int *datos=(int*)arg;
     static int mayor;
     mayor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]>mayor){
                mayor=datos[n];
        }
    }
    pthread_exit((void*)&mayor);
}

void imprimir(int *datos){
    register int n;
    for(n=0;n<N;n++){
        if(!(n%16)){ 
            printf("\n");
        }
        printf("%4.d ",datos[n]);
    }
}

void llenarArreglo(int *datos){
    register int n;
    for(n=0;n<N;n++){
        datos[n]= rand() % 4096;
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