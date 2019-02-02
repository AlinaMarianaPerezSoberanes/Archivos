//Investigar la máscara del Gaussiano con 25/04/2018
#include <stdio.h>
#include <stdlib.h>
#include "imagen.h"
#define DIMASK 3
//Un pixel ocupa un byte para reducir el tamaño de la imagen
unsigned char* RGBToGray(unsigned char *imagen,uint32_t width, uint32_t height);
void GraytoRGB(unsigned char* imagenRGB, unsigned char* imagenGray,uint32_t width, uint32_t height);
void brilloImagen(unsigned char* imagenGray,uint32_t width, uint32_t height);
void filtroPB(unsigned char* imagenO,unsigned char* imagenP,uint32_t width, uint32_t height);
unsigned char* reservarMemoria(uint32_t width, uint32_t height );

int main(){
    bmpInfoHeader info;
    unsigned char *imagenRGB;                    //para leer la imagen a colores en valores RGB dentro de la imagen
    unsigned char *imagenGray;                  // en esta imagen se guarda con un tamaño pequeño, cada pixel ocupa 1 byte en memoria
    unsigned char *imagenAux;
    imagenRGB=abrirBMP("huella1.bmp",&info);
    displayInfo(&info);
    imagenGray=RGBToGray(imagenRGB,info.width,info.height);
    //brilloImagen(imagenGray, info.width,info.height);
    imagenAux=reservarMemoria(info.width,info.height);
    filtroPB(imagenGray, imagenAux,info.width,info.height);
    //GraytoRGB(imagenRGB,imagenGray, info.width,info.height);
    GraytoRGB(imagenRGB,imagenAux, info.width,info.height);
    guardarBMP("huellaPB.bmp",&info,imagenRGB);
    free(imagenRGB); 
    free(imagenGray);    
}

void filtroPB(unsigned char* imagenO,unsigned char* imagenP,uint32_t width, uint32_t height){
    register int y,x,ym,xm;
    int conv, indiceI,indiceM;
    unsigned char mascara[DIMASK*DIMASK]={1,1,1,
                                          1,1,1,
                                          1,1,1};
    for(y=0; y<height-DIMASK;y++){                                      //recorrer mascara en la imagen
        for(x=0; x<width-DIMASK; x++){                                  //recorrer mascara en la imagen
            conv=0;
            for(ym=y; ym<y+DIMASK; ym++){                               //recorrer mascara para operaciones
                for(xm=x; xm<x+DIMASK; xm++){                           //recorrer mascara con operaraciones
                    indiceI=ym*width+xm;                                //indice de la imagen
                    indiceM=(ym-y)*DIMASK+(xm-x);                       //indice de la mascara
                    conv+=imagenO[indiceI] * mascara[indiceM];          //convolucion
                }                                                
            }
            conv/=9;                                                    //Dividir la mascar  
            indiceI=(y+1)*width+(x+1);
            imagenP[indiceI]=conv;
        }
    }                                      
}

unsigned char* reservarMemoria(uint32_t width, uint32_t height ){
    unsigned char * imagen;
    //reservamos espacio para la nueva imagen del tamaño de los piexeles contenidos
    imagen=(unsigned char*)malloc(width*height*sizeof(unsigned char));
    if(imagen==NULL){
        perror("Error");
        exit(EXIT_FAILURE);
    }
    return imagen;
}



void brilloImagen(unsigned char* imagenGray,uint32_t width, uint32_t height){
    register int x,y;
    int indice,brillo;
    for(y=0;y<height;y++){
        for(x=0;x<width;x++){
            indice=(y*width+x);
            brillo=imagenGray[indice]+40;
            imagenGray[indice]=(brillo>255)?255:brillo;

        }
    }
}


void GraytoRGB(unsigned char* imagenRGB, unsigned char* imagenGray,uint32_t width, uint32_t height){
   register int x,y;
    int indiceRGB,indiceGray;
    unsigned char nivelGris;

    for(y=0;y<height;y++){
        for(x=0;x<width;x++){
            indiceGray=(y*width+x);
            indiceRGB=indiceGray*3; //pixel en forma lineal se le suma el tamaño del wodth  y se multiplica por 3 por los pixeles rgb
            //compensasion por la longitud de onda de cada color
            nivelGris=imagenGray[indiceGray];
            imagenRGB[indiceRGB]=nivelGris;
            imagenRGB[indiceRGB+1]=nivelGris;
            imagenRGB[indiceRGB+2]=nivelGris;
        }
    } 
}

unsigned char* RGBToGray(unsigned char *imagenRGB,uint32_t width, uint32_t height){
    register int x,y;
    int indiceRGB,indiceGray;
    unsigned char nivelGris;
    unsigned char *imagenGray;
    imagenGray=reservarMemoria(width,height);
    for(y=0;y<height;y++){
        for(x=0;x<width;x++){
            indiceGray=(y*width+x);
            indiceRGB=indiceGray*3; //pixel en forma lineal se le suma el tamaño del wodth  y se multiplica por 3 por los pixeles rgb
            //compensasion por la longitud de onda de cada color
            nivelGris=((imagenRGB[indiceRGB]*11)+(imagenRGB[indiceRGB+1]*59)+(imagenRGB[indiceRGB+2]*30))/100; //se guarda como bgr 
            imagenGray[indiceGray]=nivelGris;
        }
    }
    return imagenGray;
}


