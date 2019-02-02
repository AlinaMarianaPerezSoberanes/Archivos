/*tokens.h*/
#define ENTERO 260
#define REAL 261
#define IF 262
#define THEN 263
#define BEG 264
#define END 265
#define PROCEDURE 266
#define FUNCTION 267
#define ID 268

/* ej2.l*/
%option noyywrap
%{
    #include <math.h>
    #include <stdio.h>
    #include "tokens.h"
    typedef union lexema lexemna;

	union lexema{
		int i;
		float f;
		char s[200];	
	}u;	
%}

DIGITO [0-9]
ID [a-z0-9]*

%%
{DIGITO}+    {u.i=atoi(yytext);
		return ENTERO;}

{DIGITO}+"."{DIGITO}* {u.f=atof(yytext);
			return REAL;}

"if" {return IF;}
"then" {return THEN;}
"begin" {return BEG;}
"end" {return END;}
"procedure" {return PROCEDURE;}
"function" {return FUNCTION;}
{ID} {strcpy(u.s,yytext); return ID;}
"+" {return "+";} 
"-" {return "-";} 
"*" {return "*";} 
"/" {return "/";}
"{"[^}\n]*"}" //Cualquier cosa que no sea } \n
[ \n\t]+
printf("caracter no reconocido %s \n",yytext);
%%

int main (int argc, char **argv){
	
	int tok=0;
	++argv,--argc; //deja los argumentos en 1
	if(argc>0){
		yyin=fopen(argv[0],"r");
	}else{
		yyin=stdin; //teclado
	}
	while(tok=yylex()){
		switch(tok){
			case ENTERO:
				printf("un entero %d \n", u.i);
			break;
			case REAL:
				printf("un real %g \n", u.f);
			break;
			case ID:
				printf("un id %g \n", u.s);
			break;
			case IF:
				printf("un if %g \n", yytext);
			break;
			case BEG:
				printf("un begin %g \n", yytext);
			break;
			case THEN:
				printf("un then %g \n", yytext);
			break;
			case END:
				printf("un end %g \n", yytext);
			break;
			case FUNCTION:
				printf("un function %g \n", yytext);
			break;
			case PROCEDURE:
				printf("un procedure %g \n", yytext);
			break;
			case "+":
				printf("un + %g \n", yytext);
			break;
		}
	}
return 0;
} 












