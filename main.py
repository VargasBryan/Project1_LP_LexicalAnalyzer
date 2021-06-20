import ply.lex as lex

reserved = {   #Carlos Moncayo
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
    'Array':'ARRAY',
    'String':'STRING',
    'toString':'TOSTRING',
    'undefined':'UNDEFINED',
    'length':'LENGTH',
    'Set':'SET',
    'Map':'MAP'
}
# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NAME'
)+tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A regular expression rule with some action code


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NAME(t):   #Carlos Moncayo
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
        break      # No more input
    print(tok)
