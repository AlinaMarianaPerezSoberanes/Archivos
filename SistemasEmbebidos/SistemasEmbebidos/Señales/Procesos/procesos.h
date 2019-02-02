#ifndef HILOS_H
#define HILOS_H
#include "defs.h"
extern void procesoHijo(int np, int pipefd[]);
extern void procesoPadre(int pipefd[NUM_PROC][2]);
#endif