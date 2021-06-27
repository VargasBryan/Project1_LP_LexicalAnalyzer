# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens

""""""
def p_expression_plus(p):
    'expression : expression SUMA expression'
    if (len(p) == 5):
        p[0] = p[1] + (-p[3])
    elif (len(p) == 4):
        p[0] = p[1] + p[3]

def p_expressions_minus(p):
    '''expression : expression RESTA expression
               | RESTA expression'''
    if (len(p) == 4):
     p[0] = p[1] - p[3]
    elif (len(p) == 3):
     p[0] = -p[2]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MULTIPLICACION factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
    p[0] = p[2]

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

""""
expression: expression + term
| expression - term
| term

term: term * factor
| term / factor
| factor

factor: NUMBER
| (expression)
"""