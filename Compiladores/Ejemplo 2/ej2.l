
           /* escáner para un lenguaje de juguete al estilo de Pascal */

%option noyywrap

%{
/* se necesita esto para la llamada a atof() más abajo */
#include <math.h>
#include "tokens.h"
typedef union lexema lexema;

union lexema{
  int i;
  float f;
  char s[200];
} u;

%}

DIGITO   [0-9]
ID       [a-z][a-z0-9]*

%%

{DIGITO}+              {u.i = atoi( yytext ); return ENTERO;}

{DIGITO}+"."{DIGITO}*  {u.f = atof( yytext ); return REAL;}

"if"                     {return IF;} 
"then"                   {return THEN;}
"begin"                  {return BEG;}
"end"                    {return END;}
"procedure"              {return PROCEDURE;}
"function"               {return FUNCTION;}

{ID}                   {strcpy(u.s,yytext); return ID;}

"+"                    {return '+';}
"-"                    {return '+';}
"*"                    {return '+';}
"/"                    {return '+';}

"{"[^}\n]*"}"          /* se come una linea de comentarios */

[ \t\n]+               /* se come los espacios en blanco */

.           printf( "Caracter no reconocido: %s\n", yytext );

%%

int main(int argc, char **argv )
{
int tok = 0;

   ++argv, --argc;  /* se salta el nombre del programa */
   if ( argc > 0 )
      yyin = fopen( argv[0], "r" );
   else
      yyin = stdin;

while((tok = yylex())){
   switch(tok){
     case ENTERO:
        printf( "Un entero: %d\n", u.i); break;
     case REAL:
        printf( "Un real  : %g.2\n",u.f); break;
     case IF:
     case THEN:
     case BEG:
     case END:
     case PROCEDURE:
     case FUNCTION:
        printf("Una palabra clave: %s\n",yytext ); break;
     case ID:
        printf( "Un identificador: %s\n",u.s); break;
     case '+':
     case '-':
     case '*':
     case '/':
        printf( "Un operador: %s\n", yytext ); break;

   }

 }
   return 1;
}

