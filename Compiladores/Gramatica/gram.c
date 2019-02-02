#include <stdio.h>
#include <ctype.h>
#include <string.h>
int Tprima();
int E();
int Sprima();
int T();
	int token;
	char entrada[]={'3','\0'};

int main(){
	for(int i=0;i<strlen(entrada);i++){
		Sprima();
	}
	
	return 0;
}

int Sprima(){
	int e;
	e=E();
	char aux=entrada[token];
	if((e==1) && aux=='\0'){
		printf("\nAnalisis correcto \n");
		return 1;
	}else{
		if(aux=='\0'){
			printf("\nError se esperaba un fin de cadena");
			return 0;
		}
	}
}
int E(){
	int i,k;
	i=T();
	if(i==1){
		token++;
		return 1;
	}else{
		k=Tprima();
		token++;
		return k;
	}
}
int T(){
	if(isdigit(entrada[token])){
		token++;
		return 1;
	}else{
		printf("\nSe esperaba un entero");
		token++;
		return 0;
	}
}
int Tprima(){
	if(entrada[token]==43){	
		token++;
		return E();
	}
	if(entrada[token]=='\0'){
		return 1;
	}else{
		printf("Se esperaba + o $");
		return 0;
	}	
}
