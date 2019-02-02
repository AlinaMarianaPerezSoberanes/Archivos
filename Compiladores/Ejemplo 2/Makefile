ej2: tokens.h lex.yy.c
	gcc -o ej2b lex.yy.c
lex.yy.c: ej2b.l tokens.h
	flex ej2b.l
clean:
	rm lex.yy.c ej2b *.o

