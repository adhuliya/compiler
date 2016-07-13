# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'REMAINDER',
    'POWER',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'TIMES_ASSIGN',
    'DIVIDE_ASSIGN',
    'REMAINDER_ASSIGN',
    'POWER_ASSIGN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER   = r'\*\*'
t_REMAINDER = r'%'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','

t_ASSIGN  = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_REMAINDER_ASSIGN = r'%='
t_POWER_ASSIGN = r'\*\*='


def t_ID(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d*\.\d+|\d+\.\d*|\d+'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '{}'".format(t.value[0]))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
#lexer = lex.lex(debug=1)


################################################################
# Code to test
################################################################

def tokenize(inptline):
    global lexer
    lexer.input(inptline)
    for tok in lexer:
        yield tok

################################################################
