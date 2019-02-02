
%option noyywrap
    //hola mundo
    int num_lineas=0, num_caracteres=0, numpal=0;
%%
[ \t]+ ++numpal;
\n ++num_lineas;++num_caracteres;++numpal;
. ++num_caracteres;/*[a-z]+ ++numpal;++num_caracteres; printf("Encontre una o mas letras\n");*/
%%
int main(){
    yylex();
    printf("# de lineas= %d, \n # de caracteres= %d \n # de palabras= %d\n",num_lineas,num_caracteres,numpal);

}
