grammar Ejercicio1;

// Reglas sintacticas
programa              : sentencia+ EOF ;

sentencia             : stCrear 
                      | stBuscar 
                      | stActualizar 
                      | stEliminar ;

stCrear        : 'GUARDAR' objetoJson 'EN' IDENTIFICADOR ';' ;

stBuscar       : 'BUSCAR' 'EN' IDENTIFICADOR ('DONDE' condicion)? ';' ;

stActualizar   : 'ACTUALIZAR' IDENTIFICADOR 'CON' objetoJson ('DONDE' condicion)? ';' ;

stEliminar     : 'ELIMINAR' 'DE' IDENTIFICADOR ('DONDE' condicion)? ';' ;

// Estructura de datos
objetoJson               : '{' (parClaveValor (',' parClaveValor)*)? '}' ;
parClaveValor         : CADENA ':' valor ;
valor                 : CADENA | NUMERO | BOOLEANO | objetoJson ;

condicion             : IDENTIFICADOR op=('<'|'>'|'=='|'!='|'<='|'>=') valor ;

// Reglas lexicas
BOOLEANO              : 'verdadero' | 'falso' ;
IDENTIFICADOR         : [a-zA-Z_][a-zA-Z0-9_]* ;
CADENA                : '"' ~'"'* '"' ; // Textos entre comillas
NUMERO                : [0-9]+ ('.' [0-9]+)? ;
WS                    : [ \t\r\n]+ -> skip ; // Ignorar espacios en blanco