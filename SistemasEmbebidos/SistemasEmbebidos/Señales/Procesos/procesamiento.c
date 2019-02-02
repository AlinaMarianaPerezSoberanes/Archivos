#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "defs.h"

void genera_seno(float seno[]){
	float f=1000,fs=45000;
	register int n;
	for(n=0;n<MUESTRAS;n++){
		seno[n]=sinf((2*n*M_PI*f)/fs);
	}
}
void genera_ham(float ham[]){
	//float f=1000,fs=45000;
	register int n;
	for(n=0;n<MUESTRAS;n++){
		ham[n]=0.54+0.46*cos(((2*n-MUESTRAS+1)*M_PI)/MUESTRAS);
	}
}

