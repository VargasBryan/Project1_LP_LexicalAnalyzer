import ply.lex as lex

reserved = {  # Carlos Moncayo
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'boolean': 'BOOLEAN',
    'break': 'BREAK',
    'case': 'CASE',
    'char': 'CHAR',
    'class': 'CLASS',
    'default': 'DEFAULT',
    'else': 'ELSE',
    'false': 'FALSE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'let': 'LET',
    'if': 'IF',
    'true': 'TRUE',
    'new': 'NEW',
    'static': 'STATIC',
    'const': 'CONST',
    'switch': 'SWITCH',
    'typeof': 'TYPEOF',
    'while': 'WHILE',
    'null': 'NULL',
    'var': 'VAR',
    'float': 'FLOAT',
    'return': 'RETURN',
    'int': 'INT',
    'Array': 'ARRAY',
    'String': 'STRING',
    'toString': 'TOSTRING',
    'undefined': 'UNDEFINED',
    'length': 'LENGTH',
    'Set': 'SET',
    'Map': 'MAP'
}
# List of token names.   #Bryan Vargas
tokens = (
             'POINT',
             'COLON',
             'COMMA',
             'SEMICOLON',
             'OPEN_PARENTHESIS',
             'CLOSE_PARENTHESIS',
             'OPEN_BRACKET',
             'CLOSE_BRACKET',
             'OPEN_BRACE',
             'CLOSE_BRACE',
             'LINE_BREAK',
             'SINGLE_QUOTE',
             'DOUBLE_QUOTES',
             'BACKSLASH',
         ) + tuple(reserved.values())

# Maria Rivera

# Asignaciones
def IGUAL(t):
    r'='
    return t

def t_MASIGUAL(t):
    r'\+='
    return t

def t_MENOSIGUAL(t):
    r'=='
    return t

def t_PORIGUAL(t):
    r'\*='
    return t

def t_DIVIGUAL(t):
    r'/='
    return t

def t_MODIGUAL(t):
    r'%='
    return t

def t_POTIGUAL(t):
    r'%='
    return t

# Operadores de comparación
def IGUALIGUAL(t):
    r'=='
    return t

def DIFERENTE(t):
    r'!='
    return t

def MAYORQUE(t):
    r'>'
    return t

def MAYORIGUALQUE(t):
    r'>='
    return t

def MENORQUE(t):
    r'<'
    return t

def MENORIGUALQUE(t):
    r'<='
    return t

# Operadores Aritméticos
def t_SUMA(t):
    r'\+'
    return t

def t_RESTA(t):
    r'-'
    return t

def t_MULTIPLICACION(t):
    r'\*'
    return t

def t_DIVISION(t):
    r'/'
    return t

# Operadores lógicos
def t_AND(t):
    r'&&'
    return t

def t_OR(t):
    r'||'
    return t

def t_NOT(t):
    r'\!'
    return t

precedencia = (
    ('IZQUIERDA', 'SUMA', 'RESTA'),
    ('IZQUIERDA', 'MULTIPLICACION', 'DIVISION'),
    ('DERECHA', 'NEGACION'),
)

nombres = {}

def p_ASIGNACION(p):
    nombres[p[1]] = p[3]

def p_DECLARACION(p):
    print(p[1])

def p_EXPRESION_ARITMETICA(p):
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_NEGACION(p):
    p[0] = -p[2]

def p_NUMBER(p):
    p[0] = p[1]

# Maria Rivera

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):  # Carlos Moncayo
    r'[a-zA-Z_\$]{1}[a-zA-Z0-9_\$]*'
    t.type = reserved.get(t.value, 'NAME')
    t.value = str(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# To use the lexer, you first need to feed it some input text using its input() method. After that, repeated calls to token() produce tokens. The following code shows how this works:


# Test it out
data = '''
3 + 4 * 10
+ -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
