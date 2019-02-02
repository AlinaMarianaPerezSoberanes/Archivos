typedef union {
   int pos;
   int ival;
   double fval[20];
   string sval;
   int n;
} YYSTYPE;
#define	ID	258
#define	STRING	259
#define	INT	260
#define	DESPLIEGA 261
#define SI        262
#define OTRO      263
#define AND       264 
#define OR        265 
#define NOT       266 
#define DIFER     267 
#define IGUAL     268 
#define ENTERO    269
#define COMENTARIO    270
#define DOUBLE    271
extern YYSTYPE yylval;
