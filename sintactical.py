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
    | controlStruct expression
    | methodsSet'''

def p_variable_expr(p): #Carlos Moncayo y Maria Rivera
    '''variable : type NAME IGUAL datatype SEMICOLON
    | NAME arrayFn'''

def p_controlStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''controlStruct : while
    | for'''

def p_dataStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''dataStruct : array
    | set '''

def p_while_expr(p):   #Carlos Moncayo
    '''while : WHILE OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'''

def p_comparacion_expr(p):
    '''comparacion : IGUALIGUAL
    | DIFERENTE
    | MAYORQUE
    | MAYORIGUALQUE
    | MENORQUE
    | MENORIGUALQUE'''

def p_controlArg_expr(p):
    '''controlArg : argUnico comparacion argUnico'''
def p_for_expr(p):  #Bryan Vargas
    'for : FOR OPEN_PARENTHESIS inicialization SEMICOLON condition SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE '

def p_inicialization(p):   #Bryan Vargas
    '''inicialization : type NAME IGUAL NUMBER
    | NAME IGUAL NUMBER'''

def p_condition(p):    #Bryan Vargas
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

def p_arrayFn_expr(p):
    '''arrayFn : POINT POP OPEN_PARENTHESIS CLOSE_PARENTHESIS
    | POINT PUSH OPEN_PARENTHESIS argUnico CLOSE_PARENTHESIS
    | POINT UNSHIFT OPEN_PARENTHESIS argUnico CLOSE_PARENTHESIS'''

def p_argUnico_expr(p):
    '''argUnico : NUMBER
    | STRING
    | NAME'''
def p_set_expr(p):  #Bryan Vargas
    '''set : type NAME IGUAL NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON
    | type NAME IGUAL NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON
    | type NAME IGUAL NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON
    | NAME IGUAL NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON
    | NAME IGUAL NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON
    | NAME IGUAL NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON'''

def p_methodsSet_expr(p):  #Bryan Vargas
    '''methodsSet : NAME POINT ADD OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON
    | NAME POINT DELETE OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON
    | NAME POINT CLEAR OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON
    '''

def p_items_expr(p):  #Carlos Moncayo y Maria Rivera
    '''items : numeros
    | cadena'''

def p_numeros_expr(p):   #Carlos Moncayo y Maria Rivera
    '''numeros : NUMBER
    | NUMBER COMMA numeros'''

def p_cadena_expr(p):   #Carlos Moncayo y Maria Rivera
    '''cadena : STRING 
    | STRING COMMA cadena'''

def p_element_expr(p):  #Bryan Vargas
    '''element : STRING
    | NUMBER
    | NAME'''

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
