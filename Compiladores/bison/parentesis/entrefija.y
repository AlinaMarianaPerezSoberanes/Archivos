

    /* Reverse polish notation calculator.  */

%{
       #define YYSTYPE double
       #include <math.h>
       #include <stdio.h>
       #include <math.h>
       int yylex (void);
       void yyerror (char const *);
%}

%token NUM
%left '+' '-'
%left '(' ')'
%left '*' '/'
%right '^'
%% /* Grammar rules and actions follow.  */

input:    /* empty */
             | input line
;

line:     '\n'
        | lista '\n'      { printf ("Lista aceptada: \n"); }
;

lista:   NUM
             | lista ',' NUM 
             |'(' lista ')'
             |'(' lista ')''(' lista ')'
             | lista ',' '(' lista ')'
             |'('')'
;

     %%
     #include <ctype.h>
     #include <stdio.h>

     int
     yylex (void)
     {
       int c;

       /* Skip white space.  */
       while ((c = getchar ()) == ' ' || c == '\t')
         ;
       /* Process numbers.  */
       if (isdigit (c))
         {
           ungetc (c, stdin);
           scanf ("%lf", &yylval);
           return NUM;
         }
       /* Return end-of-input.  */
       if (c == EOF)
         return 0;
       /* Return a single char.  */
       return c;
     }

     /* Called by yyparse on error.  */
     void
     yyerror (char const *s)
     {
       fprintf (stderr, "%s\n", s);
     }




     int main (void)
     {
       return yyparse ();
     }


