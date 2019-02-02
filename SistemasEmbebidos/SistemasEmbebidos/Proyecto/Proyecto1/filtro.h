
#ifndef FILTRO_H
#define FILTRO_H
#include "imagen.h"
#define DIMASK 3
#define NUM_HILOS 4
unsigned char* RGBToGray(unsigned char *imagen,uint32_t width, uint32_t height);
void GraytoRGB(unsigned char* imagenRGB, unsigned char* imagenGray,uint32_t width, uint32_t height);
void brilloImagen(unsigned char* imagenGray,uint32_t width, uint32_t height);
unsigned char* reservarMemoria(uint32_t width, uint32_t height );
void * funHilo(void *arg);
#endif