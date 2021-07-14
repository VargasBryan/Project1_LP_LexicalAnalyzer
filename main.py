import ply.lex as lex
error=[]
"""methods = {
    'add': 'ADD',
    'clear': 'CLEAR',
    'delete': 'DELETE',
    'get': 'GET',
    'has': 'HAS',
    'pop': 'POP',
    'push': 'PUSH',
    'unshift': 'UNSHIFT'
}
"""
reserved = {  # Carlos Moncayo
    #Words
    'char': 'CHAR',
    'const': 'CONST',
    'else': 'ELSE',
    'else if': 'ELSEIF',
    'false': 'FALSE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'let': 'LET',
    'if': 'IF',
    'new': 'NEW',
    'return': 'RETURN',
    'true': 'TRUE',
    'var': 'VAR',
    'while': 'WHILE',
    #Objects
    'Array': 'ARRAY',
    'Map': 'MAP',
    'Set': 'SET',
    'String': 'STRING',
    #Methods
    'add': 'ADD',
    'clear': 'CLEAR',
    'delete': 'DELETE',
    'get': 'GET',
    'has': 'HAS',
    'pop': 'POP',
    'push': 'PUSH',
    'unshift': 'UNSHIFT'
}

# List of token names.   #Bryan Vargas
tokens = (
    'COMMENTS',
    'INTEGER',
    'FLOAT',
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
    'IGUAL',
    'MASIGUAL',
    'MENOSIGUAL',
    'PORIGUAL',
    'DIVIGUAL',
    'MODIGUAL',
    'POTIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'MAYORQUE',
    'MAYORIGUALQUE',
    'MENORQUE',
    'MENORIGUALQUE',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'AND',
    'NOT',
    'OR',
    'LONGCOMMENT',
    'NAME',
    'PRINT'
) + tuple(reserved.values()) #  + tuple(methods.values())

# Maria Rivera

def t_STRING(t):
    r'\".*\"'
    return t

def t_CHAR(t):
    r'\".\"'
    return t

# Asignaciones
t_POINT = r'\.'
t_COLON = r':'
t_COMMA = r','
t_SEMICOLON = r';'
t_OPEN_PARENTHESIS = r'\('
t_CLOSE_PARENTHESIS = r'\)'
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'

def t_MASIGUAL(t):
    r'\+='
    return t


def t_MENOSIGUAL(t):
    r'-='
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
    r'\*\*='
    return t

# Operadores de comparación


def t_IGUALIGUAL(t):
    r'=='
    return t


def t_DIFERENTE(t):
    r'!='
    return t

def t_MAYORIGUALQUE(t):
    r'>='
    return t


def t_MENORIGUALQUE(t):
    r'<='
    return t

def t_COMMENTS(t):
    r'//.*'
    pass

def t_LONGCOMMENT(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')
    pass

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

def t_IGUAL(t):
    r'='
    return t
    
# Operadores lógicos

def t_MENORQUE(t):
    r'<'
    return t

def t_MAYORQUE(t):
    r'>'
    return t
def t_AND(t):
    r'&&'
    return t


def t_OR(t):
    r'[|]{2}'
    return t


def t_NOT(t):
    r'\!'
    return t

# Maria Rivera

# A regular expression rule with some action code

def t_PRINT(t):
    r'console\.log'
    return t

def t_FLOAT(t):
    r'\d+ \. \d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
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
    error.append("Illegal character "+str(t.value[0]))
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# To use the lexer, you first need to feed it some input text using its input() method. After that, repeated calls to token() produce tokens. The following code shows how this works:

# Test it out

data = '''
for(a:4);
pop
delete
1
@
19.3
'''

# Give the lexer some input
lexer.input(data)

""" # Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok) """
