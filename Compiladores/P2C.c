#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define ID 1
#define NUM 2;
#define ERROR 0;
#define OPERADORES 4;

int main(){

    char linea[100];
    char car;
    int edo=0;
    FILE *f;
	f = fopen ( "/home/alina/Documents/archivo.txt", "r" );        
	if (f==NULL){
        fputs ("File error",stderr);
    }
    fgets (linea, 100, f);
    for(int i=0;i<50;i++){
        car=linea[i];
        switch(edo){
            case 0: 
                if(isalpha(car)){
                    printf("Encontre un ID %c : Estado %d : \n ",car,edo);
                    edo=1;                 
                    continue;
                }
                if(isdigit(car)){
                    printf("Encontre un NUM %c : Estado %d : \n ",car,edo);
                    edo=2;
                    continue;
                }
                if(isblank(car)){
                    printf("Encontre un blanco %c : Estado %d : \n ",car,edo);
                    edo=3;
                    continue;
                }
                if(car==33 || car==38 || car==43 || car==45 || car==42 || car==60 || car==61 || car==62){
                   printf("Encontre un OP %c : Estado %d : \n ",car,edo);
                    edo=4;
                    continue; 
                }
                if(car==39 || car==40 || car==41 || car==34 || car==91 || car==93 || car==123 || car==125){
                   printf("Encontre un CIERRE %c : Estado %d : \n ",car,edo);
                    edo=5;
                    continue; 
                }else{
                   printf("Encontre un Otro %c : Estado %d : \n ",car,edo);
                    edo=6;
                    continue;  
                }       
            case 1:
                if(isalpha(car)){
                    printf("Encontre un ID %c : Estado %d : \n ",car,edo);
                    edo=1;
                    //ungetc (car, f);
                    continue;
                }else{
                    edo=0;
                }
            case 2: 
                if(isdigit(car)){
                    printf("Encontre un NUM %c : Estado %d : \n ",car,edo);
                    edo=2;
                    //ungetc (car, f);
                    continue;
                }else{
                    edo=0;  
                }
            case 3:
                if(isblank(car)){
                    printf("Encontre un blanco %c : Estado %d : \n ",car,edo);
                    edo=3;
                    continue;
                }else{
                    edo=0;                   
                }
            case 4:
                if(car==33 || car==38 || car==43 || car==45 || car==42 || car==60 || car==61 || car==62){
                    printf("Encontre un OP %c : Estado %d : \n ",car,edo);
                    edo=4;
                    continue;
                }else{
                    edo=0;                  
                }
            case 5:
                if(car==39 || car==40 || car==41 || car==34 || car==91 || car==93 || car==123 || car==125){
                   printf("Encontre un CIERRE %c : Estado %d : \n ",car,edo);
                    edo=5;
                    continue; 
                }else{
                    edo=0;                  
                }
            default:
                    edo=0;
                    continue; 
                    
                
        }
        
    }
    return 0;
}