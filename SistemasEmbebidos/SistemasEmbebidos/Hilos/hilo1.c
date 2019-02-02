#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void *suma(void *arg);
void *resta(void *arg);
void *multi(void *arg);
void *division(void *arg);
int n1=60;
int n2=12;

int main(){
    int *res_suma,*res_resta,*res_multi,*res_divi;
    pthread_t tid_s,tid_r,tid_m,tid_d;
   
    pthread_create(&tid_s,NULL,suma,NULL);        //crea el nuevo hilo
    pthread_create(&tid_r,NULL,resta,NULL);        //crea el nuevo hilo
    pthread_create(&tid_m,NULL,multi,NULL);        //crea el nuevo hilo
    pthread_create(&tid_d,NULL,division,NULL);        //crea el nuevo hilo
   
    pthread_join(tid_s,(void**)&res_suma);        //espera a que termine la ejecucion del hilo
    pthread_join(tid_r,(void**)&res_resta);
    pthread_join(tid_m,(void**)&res_multi);
    pthread_join(tid_d,(void**)&res_divi);

    printf("La suma es: %d\n",*res_suma);
    printf("La resta es: %d\n",*res_resta);
    printf("La miltiplicacion es: %d\n",*res_multi);
    printf("La division es: %d\n",*res_divi);
    return 0;
}

void *suma(void *arg){
    static int res;
    res=n1+n2;
    pthread_exit((void*)&res);                  //se hace el cast a void
}
void *resta(void *arg){
    static int res;
    res=n1-n2;
    pthread_exit((void*)&res);                  //se hace el cast a void
}
void *multi(void *arg){
    int *res=(int*)malloc(sizeof(int));
    *res=n1*n2;
    pthread_exit((void*)res);                  //se hace el cast a void
}
void *division(void *arg){
    int *res=(int*)malloc(sizeof(int));
    *res=n1/n2;
    pthread_exit((void*)res);                  //se hace el cast a void
}
