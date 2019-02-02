#ifndef PROCESOS_H
#define PROCESOS_H
#include "defs.h"
void procesoHijo(int np, int pipefd[]);
void procesoPadre(int pipefd[]);
void imprimir(int *datos);
void llenarArreglo(int *datos);
int *reservarMemoria(void);
#endif