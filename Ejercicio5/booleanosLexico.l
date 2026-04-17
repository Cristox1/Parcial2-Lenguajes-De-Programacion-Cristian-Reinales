%{
#include "booleanosSintactico.tab.h" 
extern int yylval;
%}

%option case-insensitive

%%
true|1          { yylval = 1; return VALOR; }
false|0         { yylval = 0; return VALOR; }
and|"&"         { return AND; }
or|"|"          { return OR; }
not|"!"         { return NOT; }
"("             { return '('; }
")"             { return ')'; }
\n              { return '\n'; }
[ \t]           { /* ignorar espacios en blanco */ }
.               { printf("Caracter no reconocido: %s\n", yytext); }
%%

int yywrap() { return 1; }