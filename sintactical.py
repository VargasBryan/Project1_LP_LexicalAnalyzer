# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens

def p_expression_expr(p):
    '''expression : variable
    | variable expression
    | dataStruct
    | dataStruct expression
    | controlStruct
    | controlStruct expression'''

def p_variable_expr(p):
    'variable : type NAME IGUAL datatype SEMICOLON'

def p_controlStruct_expr(p):
    'controlStruct : while'

def p_dataStruct_expr(p):
    'dataStruct : array'

def p_while_expr(p):
    '''while : WHILE OPEN_PARENTHESIS expression CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'''

def p_operations(p):
    '''operations : NUMBER operand NUMBER'''

def p_datatype_expr(p):
    '''datatype : NUMBER
    | STRING
    | operations
    | CHAR'''

def p_operand_expr(p):
    '''operand : SUMA 
    | RESTA 
    | MULTIPLICACION 
    | DIVISION'''

def p_bool_expr(p):
    '''bool : TRUE
    | FALSE'''

def p_type_expr(p):
    '''type : CONST
    | LET
    | VAR'''

""" def p_object_expr(p):
    '''object : char
    | array
    | map
    | set
    | NUMBER
    | STRING
    | NULL''' """

def p_array_expr(p):
    '''array : type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON
    | type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLON'''


def p_items_expr(p):
    '''items : numeros
    | cadena'''

def p_numeros_expr(p):
    '''numeros : NUMBER
    | NUMBER COMMA numeros'''

def p_cadena_expr(p):
    '''cadena : STRING
    | STRING COMMA cadena'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)

""" "
expression: expression + term
| expression - term
| term

term: term * factor
| term / factor
| factor

factor: NUMBER
| (expression)
 """