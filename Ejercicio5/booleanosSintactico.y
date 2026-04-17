%{
#include <stdio.h>
void yyerror(const char *s);
int yylex(void);
%}

%token VALOR AND OR NOT

%left OR
%left AND
%right NOT

/* Reglas de la gramatica */
%%
calculadora:
    /* vacio */
    | calculadora linea
    ;

linea:
    '\n'
    | expr '\n' { printf("Resultado: %s\n", $1 ? "True" : "False"); }
    ;

expr:
    VALOR           { $$ = $1; }
    | expr OR expr  { $$ = $1 || $3; }
    | expr AND expr { $$ = $1 && $3; }
    | NOT expr      { $$ = !$2; }
    | '(' expr ')'  { $$ = $2; }
    ;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error sintactico: %s\n", s);
}

int main(void) {
    printf("Ingrese una expresion booleana (true AND false):\n");
    return yyparse();
}