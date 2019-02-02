#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define ID 1
#define NUM 2;
#define ERROR 0;

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
                }else{
                    if(isdigit(car)){
                        printf("Encontre un NUM %c : Estado %d : \n ",car,edo);
                        edo=2;
                        continue;
                    }else{
                        if(isblank(car)){
                             printf("Encontre un blanco %c : Estado %d : \n ",car,edo);
                            edo=3;
                            continue;

                        }
                    }
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
                    //ungetc (car, f);
                    continue;
                }else{
                    edo=0;
                    
                }
        }
        
    }
    return 0;
}