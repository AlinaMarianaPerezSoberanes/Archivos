
/*Pograma anterior con los hilos con mayor menor promedio y etc*/
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define N 8192
#define NUM_HILOS 4
typedef enum{MAYOR=0,MENOR,PROMEDIO,ORDENA}TAREAS;
/*funciones*/
int *reservarMemoria(void);
void llenarArreglo(int *datos);
void imprimir(int *datos);
void mayorArreglo();
void menorArreglo();
void promediaArreglo();
void ordenarArreglo(); 
void * funHilo(void *arg);                                                 
/*globales*/
int contador;
pthread_mutex_t bloqueo; 
int *datos;
int mayor,menor,promedio; 

int main(){
    srand(time(NULL));
    datos= reservarMemoria();
    llenarArreglo(datos);
    imprimir(datos);
    int *hilo,i,k,nhs[NUM_HILOS];
    contador=0;
    pthread_mutex_init(&bloqueo,NULL);                                      //se crea el mutex
    pthread_t tids[NUM_HILOS];
    for(i=0;i<NUM_HILOS;i++){
        nhs[i]=i;                                                           //creacion de hilos
        pthread_create(&tids[i],NULL,funHilo,(void *)&nhs[i]);              //crea varios hilos
    }
    for(k=0;k<NUM_HILOS;k++){
         pthread_join(tids[k],(void**)&hilo);                               //espera a que termine la ejecucion del hilo
         printf("\nHilo %d terminado\n",*hilo);
    }
    pthread_mutex_destroy(&bloqueo);                                        //liberamos memoria del mutex 
    //resultados
    printf("El mayor es %d \nEl menor es: %d \nEl promedio es: %d \n",mayor,menor,promedio);
    imprimir(datos);                                                  
    return 0;
}
/*
void * funHilo(void *arg){
    register int i=0;
    pthread_mutex_lock(&bloqueo);
    contador++;                                                             //4g de ciclo en ejecucion para hacer un retardo
    printf("Hilo en ejecucion con contador en %d\n ",contador);
    while((--i));    
    printf("Hilo finalizando con contador en  %d\n ",contador);
    pthread_mutex_unlock(&bloqueo);                                            
    pthread_exit(arg);
}*/

void * funHilo(void *arg){
    register int i=0;
    switch(*(int*)arg){
        case MAYOR:            
                printf("\nHilo 0 en ejecucion\n");
                mayorArreglo();
                while((--i));   
        break;
        case MENOR:
            i=0;
                printf("\nHilo 1 en ejecucion \n");
                menorArreglo();
                while((--i));   
        break;
        case PROMEDIO:
            i=0;
                pthread_mutex_lock(&bloqueo); 
                printf("\nHilo 2 en ejecucion\n ");
                promediaArreglo();
                while((--i)); 
                pthread_mutex_unlock(&bloqueo);  
        break;
        case ORDENA:
            i=0;
            pthread_mutex_lock(&bloqueo);                               //Region crítica
                printf("\nHilo 3 en ejecucion\n ");
                ordenarArreglo();
                while((--i));   
            pthread_mutex_unlock(&bloqueo);
        break;
    }                                           
    pthread_exit(arg);
}

void menorArreglo(){
     register int n;
     menor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]<menor){
                menor=datos[n];
        }
    }
}

void mayorArreglo(){
     register int n;
     mayor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]>mayor){
                mayor=datos[n];
        }
    }
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
        datos[n]= rand() % 16384;
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

void ordenarArreglo(){
    register int i,j,n;
    int aux;
    for(i=0; i < N-1; i++){
        for(j=0; j < N-1; j++){
            if(datos[j] > datos[j+1]){
                aux=datos[j];
                datos[j]=datos[j+1];
                datos[j+1]=aux;
            }
        }
    }   
}

void promediaArreglo(){
    int suma=0;
    register int n;
    for(n=0;n<N;n++){
        suma=suma+datos[n];
    }
    promedio=suma>>13;
}
