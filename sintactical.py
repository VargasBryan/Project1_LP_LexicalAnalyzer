# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens

def p_expression_expr(p):  #Carlos Moncayo y Maria Rivera
    '''expression : variable
    | variable expression
    | dataStruct
    | dataStruct expression
    | controlStruct
    | controlStruct expression'''

def p_variable_expr(p): #Carlos Moncayo y Maria Rivera
    'variable : type NAME IGUAL datatype SEMICOLON'

def p_controlStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''controlStruct : while
    | for'''

def p_dataStruct_expr(p): #Carlos Moncayo y Maria Rivera
    'dataStruct : array'

def p_while_expr(p):   #Carlos Moncayo
    '''while : WHILE OPEN_PARENTHESIS expression CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'''

def p_for_expr(p):  #Bryan Vargas
    'for : FOR OPEN_PARENTHESIS inicialization SEMICOLON condition SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE '

def p_inicialization(p):    #Bryan Vargas
    '''inicialization : type NAME IGUAL NUMBER
    | NAME IGUAL NUMBER'''

def p_condition(p):     #Bryan Vargas
    'condition : NAME clause value '

def p_operations(p): #Carlos Moncayo y Maria Rivera
    '''operations : NUMBER operand NUMBER
    | NAME SUMA SUMA
    | NAME RESTA RESTA '''

def p_datatype_expr(p):  #Carlos Moncayo y Maria Rivera
    '''datatype : NUMBER
    | STRING
    | operations
    | CHAR'''

def p_operand_expr(p):    #Carlos Moncayo
    '''operand : SUMA 
    | RESTA 
    | MULTIPLICACION 
    | DIVISION'''

def p_bool_expr(p):   #Carlos Moncayo
    '''bool : TRUE
    | FALSE'''

def p_type_expr(p):   #Carlos Moncayo
    '''type : CONST
    | LET
    | VAR'''

def p_clause_expr(p):   #Bryan Vargas
    '''clause :  IGUALIGUAL
    | DIFERENTE
    | MAYORQUE
    | MAYORIGUALQUE
    | MENORQUE
    | MENORIGUALQUE '''

def p_value_expr(p):    #Bryan Vargas
    '''value : NAME
    | NUMBER'''

def p_array_expr(p):    #Carlos Moncayo
    '''array : type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON
    | type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLON'''


def p_items_expr(p):  #Carlos Moncayo y Maria Rivera
    '''items : numeros
    | cadena'''

def p_numeros_expr(p):   #Carlos Moncayo y Maria Rivera
    '''numeros : NUMBER
    | NUMBER COMMA numeros'''

def p_cadena_expr(p):   #Carlos Moncayo y Maria Rivera
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
