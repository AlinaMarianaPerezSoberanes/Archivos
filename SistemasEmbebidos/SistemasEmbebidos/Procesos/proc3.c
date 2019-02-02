//Ordenar arreglo 
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#define N 64
#define NUM_PROC 4
int *reservarMemoria(void);
void llenarArreglo(int *datos);
void imprimir(int *datos);
int mayorArreglo(int *datos);
int menorArreglo(int *datos);
void procesoHijo(int np, int *datos);
void procesoPadre();
int promediaArreglo(int *datos);
void ordenarArreglo(int *datos);

int main(){
    pid_t pid;
    register int np;
    int *datos;
    datos= reservarMemoria();
    llenarArreglo(datos);
    imprimir(datos);
    
        for(int np=0;np<NUM_PROC;np++){
            pid=fork();
            if(!pid){//Proceso hijo
                procesoHijo(np,datos);
            }
        }
        procesoPadre(np,datos); //Proceso padre 
    
    
}
void procesoPadre(){
            register int np;
            int pid,resultado;
            pid=getpid();
            
            for(np=0;np<NUM_PROC;np++){
                pid=wait(&resultado);
                printf("\nProceso hijo terminado %d con el resultado %d \n",pid,resultado>>8);
            }           
}

void procesoHijo(int np, int *datos){
    int mayor,menor, promedio;
            //pid=getpid();
            printf("\nProceso hijo con pid %d \n",getpid());
            if(np==0){
               mayor= mayorArreglo(datos);
               exit(mayor);
            }if(np==1){
                menor= menorArreglo(datos);
               exit(menor);
            }
            if(np==2){
                promedio= promediaArreglo(datos);
               exit(promedio);
            }
            if(np==3){
                ordenarArreglo(datos);
                exit(0);
            }
        
            
}

void ordenarArreglo(int *datos){
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
    imprimir(datos);

}

int promediaArreglo(int *datos){
    int suma=0;
    register int n;
    for(n=0;n<N;n++){
        suma=suma+datos[n];
    }
    //printf("SUMA: %d \n",suma);
    //printf("prom: %d \n",suma>>6);
 return suma>>6;
}

int menorArreglo(int *datos){
     register int n;
     int menor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]<menor){
                menor=datos[n];
        }
    }
    return menor;
}

int mayorArreglo(int *datos){
     register int n;
     int mayor=datos[0];
    for(n=0;n<N;n++){
        if(datos[n]>mayor){
                mayor=datos[n];
        }
    }
    return mayor;
}

void imprimir(int *datos){
    register int n;
    for(n=0;n<N;n++){
        if(!(n%16)){ 
            printf("\n");
        }
        printf("%3.d ",datos[n]);
    }
}

void llenarArreglo(int *datos){
    register int n;
    for(n=0;n<N;n++){
        datos[n]=rand()%256;
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