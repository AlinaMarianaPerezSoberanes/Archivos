
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "defs.h"

void guarda_datos(float datos[],float ham[],float res[]){
	FILE * ap_arch;
	FILE * ap_archh;
	FILE * ap_archr;
	register int n;
	ap_arch=fopen("seno.dat","w");
	ap_archh=fopen("hamming.dat","w");
	ap_archr=fopen("resultado.dat","w");
	if(!ap_arch || !ap_archh){
		perror("Error al abrir el archivo");
		exit(EXIT_FAILURE);
	}
	for(n=0;n<MUESTRAS;n++){
		fprintf(ap_arch,"%f \n",datos[n]);
		fprintf(ap_archh,"%f \n",ham[n]);
		fprintf(ap_archr,"%f \n",res[n]);
	}
	fclose(ap_arch);
	fclose(ap_archh);
}
