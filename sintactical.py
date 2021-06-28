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
    '''variable : type NAME IGUAL datatype SEMICOLON
        | type NAME IGUAL operations SEMICOLON
        | NAME IGUAL datatype SEMICOLON'''

def p_controlStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''controlStruct : while
    | if'''

def p_dataStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''dataStruct : array
        | map'''

def p_while_expr(p):   #Carlos Moncayo
    '''while : WHILE OPEN_PARENTHESIS expression CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'''

def p_if_expr(p): #Maria Rivera
    '''if : soloIf 
    | soloIf elseIf
    | soloIf elseIf else
    | soloIf else'''

def p_soloIf_expr(p): #Maria Rivera
    ' soloIf : IF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'

def p_elseIf_expr(p): #Maria Rivera
    ''' elseIf : ELSEIF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
        | ELSEIF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE soloIf'''

def p_else_expr(p): #Maria Rivera
    ' else : ELSE OPEN_BRACE expression CLOSE_BRACE'

def p_operations(p): #Carlos Moncayo y Maria Rivera
    '''operations : NUMBER operand NUMBER'''

def p_datatype_expr(p):  #Carlos Moncayo y Maria Rivera
    '''datatype : NUMBER
    | STRING
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


def p_array_expr(p):    #Carlos Moncayo
    '''array : type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON
    | type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLON'''

def p_map_expr(p):   #Maria Rivera
    '''map : iniciarMap
        | escribirMap
        | generarMap '''

def p_iniciarMap_expr(p): #Maria Rivera
    'iniciarMap : variable IGUAL NEW MAP OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON'

def p_escribirMap_expr(p): #Maria Rivera
    'escribirMap : variable IGUAL OPEN_BRACE claveValor CLOSE_BRACE'

def p_claveValor_expr(p): #Maria Rivera
    '''claveValor : clave COLON valor
    | clave COLON valor COMMA claveValor'''

def p_clave_expr(p): #Maria Rivera
    'clave : datatype'

def p_valor_expr(p): #Maria Rivera
    '''valor : datatype
        | dataStruct'''

def p_generarMap_expr(p): #Maria Rivera
     'generarMap : variable IGUAL OPEN_BRACE tuplas CLOSE_BRACE'

def p_tuplas_expr(p): #Maria Rivera
    '''tuplas : tupla
        | tupla tuplas '''

def p_tupla_expr(p): #Maria Rivera
    ''' tupla : OPEN_BRACKET datatype CLOSE_BRACKET
        | OPEN_BRACKET datatype COMMA datatype CLOSE_BRACKET'''

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
