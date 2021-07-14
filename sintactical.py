# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens

global flag
flag=0

def p_expression_expr(p):  #Carlos Moncayo y Maria Rivera
    '''expression : semiExpression
    | semiExpression expression'''

def p_semiExpression_exp(p):
    '''semiExpression : variable
    | dataStruct
    | controlStruct
    | methodsSet
    | mapFunctions
    | arrayFn
    | declaration
    | print
    | return
    | function
    | COMMENTS
    | asigOp'''

def p_number_expr(p):
    '''number : INTEGER
    | FLOAT
    | OPEN_PARENTHESIS RESTA INTEGER CLOSE_PARENTHESIS
    | OPEN_PARENTHESIS RESTA FLOAT CLOSE_PARENTHESIS'''

def p_variable_expr(p): #Carlos Moncayo y Maria Rivera
    '''variable : type NAME IGUAL datatype SEMICOLON
        | NAME IGUAL datatype SEMICOLON'''

def p_controlStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''controlStruct : while
    | for
    | if'''

def p_dataStruct_expr(p): #Carlos Moncayo y Maria Rivera
    '''dataStruct : array
    | set
    | map '''

def p_while_expr(p):   #Carlos Moncayo
    '''while : WHILE OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'''

def p_if_expr(p): #Maria Rivera
    '''if : soloIf 
    | soloIf elseIf
    | soloIf elseIf else
    | soloIf else'''

def p_soloIf_expr(p): #Maria Rivera
    ' soloIf : IF OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE'

def p_elseIf_expr(p): #Maria Rivera
    ''' elseIf : ELSEIF OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
        | ELSEIF OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE soloIf'''

def p_else_expr(p): #Maria Rivera
    ' else : ELSE OPEN_BRACE expression CLOSE_BRACE'

def p_controlArg_expr(p):
    '''controlArg : element clause element'''

def p_for_expr(p):  #Bryan Vargas
    'for : FOR OPEN_PARENTHESIS inicialization SEMICOLON expBoolean SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE '

def p_inicialization(p):   #Bryan Vargas
    '''inicialization : type NAME IGUAL number
    | NAME IGUAL number'''

def p_operations(p): #Carlos Moncayo y Maria Rivera
    '''operations : number operand number
    | NAME
    | number
    | number operand NAME operations
    | NAME operand number operations
    | number operand NAME
    | NAME operand number
    | NAME operand NAME operations
    | number operand number operand operations
    | NAME SUMA SUMA
    | NAME RESTA RESTA'''

def p_datatype_expr(p):  #Carlos Moncayo y Maria Rivera
    '''datatype : number
    | STRING
    | CHAR
    | operations
    | dataStruct'''

def p_operand_expr(p):    #Carlos Moncayo
    '''operand : SUMA 
    | RESTA 
    | MULTIPLICACION 
    | DIVISION'''

def p_operadorAsig_expr(p):
    '''operadorAsig : MASIGUAL
    | MENOSIGUAL
    | PORIGUAL
    | DIVIGUAL
    | MODIGUAL
    | POTIGUAL'''

def p_asigOp_expr(p):
    'asigOp : NAME operadorAsig number SEMICOLON'

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

"""
def p_value_expr(p):    #Bryan Vargas
    '''value : NAME
    | number'''
"""
def p_array_expr(p):    #Carlos Moncayo
    '''array : OPEN_BRACKET items CLOSE_BRACKET SEMICOLON
    | NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLON'''

def p_map_expr(p):   #Maria Rivera
    '''map : iniciarMap
        | escribirMap
        | generarMap '''

def p_iniciarMap_expr(p): #Maria Rivera
    'iniciarMap : NEW MAP OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON'

def p_escribirMap_expr(p): #Maria Rivera
    'escribirMap : OPEN_BRACE claveValor CLOSE_BRACE'

def p_claveValor_expr(p): #Maria Rivera
    '''claveValor : clave COLON datatype
    | clave COLON datatype COMMA claveValor'''

def p_clave_expr(p): #Maria Rivera
    'clave : datatype'
"""
def p_valor_expr(p): #Maria Rivera
    '''valor : datatype
        | dataStruct'''
"""
def p_generarMap_expr(p): #Maria Rivera
     'generarMap : OPEN_BRACE tuplas CLOSE_BRACE'

def p_tuplas_expr(p): #Maria Rivera
    '''tuplas : tupla
        | tupla COMMA tuplas '''

def p_tupla_expr(p): #Maria Rivera
    ''' tupla : OPEN_BRACKET datatype CLOSE_BRACKET SEMICOLON
        | OPEN_BRACKET datatype COMMA datatype CLOSE_BRACKET SEMICOLON'''

def p_mapFunctions_expr(p): #Maria Rivera
    '''mapFunctions : NAME POINT CLEAR OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON
        | NAME POINT GET OPEN_PARENTHESIS clave CLOSE_PARENTHESIS SEMICOLON
        | NAME POINT HAS OPEN_PARENTHESIS clave CLOSE_PARENTHESIS SEMICOLON'''

def p_arrayFn_expr(p):
    '''arrayFn : NAME POINT POP OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON
    | NAME POINT PUSH OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON
    | NAME POINT UNSHIFT OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON'''

def p_set_expr(p):  #Bryan Vargas
    '''set : NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON
    | NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON
    | NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON'''

def p_methodsSet_expr(p):  #Bryan Vargas
    '''methodsSet : NAME POINT ADD OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON
    | NAME POINT DELETE OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON
    | NAME POINT CLEAR OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON '''


def p_items_expr(p):  #Carlos Moncayo y Maria Rivera
    '''items : item
    | item COMMA items'''

def p_item_expr(p): #Bryan Vargas
    '''item : number
    | STRING
    | expBoolean
    | NAME
    | datatype'''

def p_cadena_expr(p):   #Carlos Moncayo y Maria Rivera
    '''cadena : STRING 
    | STRING COMMA cadena'''


def p_element_expr(p):  #Bryan Vargas
    '''element : STRING
    | number
    | NAME'''

def p_declaration_expr(p):  #Bryan Vargas
    'declaration : NAME IGUAL element SEMICOLON'

def p_logicalOperator_expr(p):   #Bryan Vargas
    '''logicalOperator : AND
    | OR'''

def p_expBoolean_expr(p):   #Bryan Vargas
    '''expBoolean : controlArg
    | bool
    | NOT expBoolean
    | expBoolean logicalOperator expBoolean'''

def p_function_expr(p):
    '''function : FUNCTION NAME OPEN_PARENTHESIS CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE
    | FUNCTION NAME OPEN_PARENTHESIS parameter CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE '''

def p_parameter_expr(p):
    '''parameter : element
    | element parameter
    '''

def p_return_expr(p):
    'return : RETURN element SEMICOLON'

def p_print_expr(p):
    'print : PRINT OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON'


# Error rule for syntax errors
def p_error(p):
    global flag
    flag=1
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def sintaxAnalisys(sentence):
    global flag
    flag =0
    result = parser.parse(sentence)
    if flag==0:
        return "No syntax error found!"
    else:
        return "Syntax error in input!"


"""
#Probar Sintactico
# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")

"""
More information on these methods is as follows:
parser.errok(). This resets the parser state so it doesn't think it's in error-recovery mode. This will prevent an error token from being generated and will reset the internal error counters so that the next syntax error will call p_error() again.
parser.token(). This returns the next token on the input stream.
parser.restart(). This discards the entire parsing stack and resets the parser to its initial state.
"""

# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
"""