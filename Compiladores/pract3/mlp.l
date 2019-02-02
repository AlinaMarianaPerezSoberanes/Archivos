

%{
#include <string.h>
#include <stdio.h>
#include "util.h"
#include "y.tab.h"
#include "errormsg.h"

int charPos=1;
 int c=0;
extern YYSTYPE yylval;

int yywrap(void)
{
 charPos=1;
 return 1;
}


void adjust(void)
{
 EM_tokPos=charPos;
 charPos+=yyleng;
}

//char bufer[256];char *apbufer;

#define MAX_STR_CONST   256
char string_buf[MAX_STR_CONST];
char *string_buf_ptr;
double lista[20];
double *lista_ptr;

%}


%x cade
%x comentario
%x listaf
%%

" "      {adjust(); continue;}
\n       {adjust(); EM_newline(); continue;}
","      {adjust(); return ',';}
";"      {adjust(); return ';';}
"="      {adjust(); return '=';}
"("      {adjust(); return '(';}
")"      {adjust(); return ')';}

"+"      {adjust(); return '+';}
"-"      {adjust(); return '-';}
"*"      {adjust(); return '*';}
"%"      {adjust(); return '%';}
">"      {adjust(); return '>';}
":"      {adjust(); return ':';}
"<"      {adjust(); return '<';}

entero     {adjust(); return ENTERO;}
despliega  {adjust(); return DESPLIEGA;}
si         {adjust(); return SI;}
otro       {adjust(); return OTRO;}

[0-9]+   {adjust(); yylval.ival=atoi(yytext); return INT;}
[a-zA-Z_][a-zA-Z0-9_]* {adjust(); yylval.sval=String(yytext); return ID;}

\{                         {adjust(); BEGIN(listaf);}
<listaf>[0-9]+[.][0-9]*    {adjust();lista[c]= atof(yytext);c++;}
<listaf>\}                 {adjust();
                             BEGIN(INITIAL);
                            for(int i=0;i<c ;i++){
                                    yylval.fval[i]=lista[i];
                                    }
                             return DOUBLE;} 

"//"+      {adjust(); string_buf_ptr = string_buf; BEGIN(comentario);}
<comentario>\n          {adjust();
                        BEGIN(INITIAL);
                        *string_buf_ptr = '\0';
                        yylval.sval=String(string_buf);
                        return COMENTARIO;}


"/*"+      {adjust(); string_buf_ptr = string_buf; BEGIN(comentario);}
<comentario>[\*\n]*    {adjust();   /* come todo lo que no sea '-' */ }
<comentario>\n         {adjust();EM_newline();}
<comentario>"*/"        {adjust();
                        BEGIN(INITIAL);
                        *string_buf_ptr = '\0';
                        yylval.sval=String(string_buf);
                        return COMENTARIO;}


\"              {adjust(); string_buf_ptr = string_buf; 
                 BEGIN(cade); }

<cade>\"        { /* se vio la comilla que cierra - todo est� hecho */
                   adjust();
                   BEGIN(INITIAL);
                   *string_buf_ptr = '\0';
                   yylval.sval=String(string_buf);
                   return STRING;
                   /* devuelve un tipo de token de cadena constante y
                    * el valor para el analizador sint�ctico
                    */
                   }

<cade>\n        {
                   /* error - cadena constante sin finalizar */
                   /* genera un mensaje de error */
                   }

<cade>\\[0-7]{1,3} {
                   /* secuencia de escape en octal */
                   adjust();
                   int resultado;

                   (void) sscanf( yytext + 1, "%o", &resultado );

                   if ( resultado > 0xff )
                           /* error, constante fuera de rango */

                   *string_buf_ptr++ = resultado;
                   }

<cade>\\[0-9]+ {
                   /* genera un error - secuencia de escape err�nea;
                    * algo como '\48' o '\0777777'
                    */
                   }

<cade>\\n    {adjust(); *string_buf_ptr++ = '\n';}
<cade>\\t    {adjust(); *string_buf_ptr++ = '\t';}
<cade>\\r    {adjust(); *string_buf_ptr++ = '\r';}
<cade>\\b    {adjust(); *string_buf_ptr++ = '\b';}
<cade>\\f    {adjust(); *string_buf_ptr++ = '\f';}

<cade>\\(.|\n)  {adjust(); EM_newline(); *string_buf_ptr++ = yytext[1];}

<cade>[^\\\n\"]+  {
                    adjust();
                    char *yptr = yytext;
                    while ( *yptr )
                           *string_buf_ptr++ = *yptr++;
                   }


          /*<<EOF>> {printf("\nFin de Archivo encontrado."); exit(0); }*/

.        {adjust(); EM_error(EM_tokPos,"token ilegal");}
