grammar PythonToJava;

// Parser Rules
program: (func_def)* EOF;

func_def: DEF NAME LPAREN params? RPAREN COLON NEWLINE stmt+;

params: NAME (COMMA NAME)*;

stmt: (var_assign | return_stmt | print_stmt) NEWLINE
    | NEWLINE;

var_assign: NAME ASSIGN expr;

return_stmt: RETURN expr;

print_stmt: PRINT LPAREN expr RPAREN;

expr: expr (MUL | DIV) expr
    | expr (PLUS | MINUS) expr
    | NUMBER
    | func_call
    | NAME
    | LPAREN expr RPAREN;

func_call: NAME LPAREN (expr (COMMA expr)*)? RPAREN;

// Lexer Rules
DEF: 'def';
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';
ASSIGN: '=';
RETURN: 'return';
PRINT: 'print';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

NAME: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;