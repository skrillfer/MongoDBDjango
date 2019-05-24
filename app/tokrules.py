# module: tokrules.py
# This module just contains the lexing rules
import sys

# List of token names.   This is always required
tokens = (
   'VAR',
   'NUMBER',
   'DSPTS',
   'COMA',
   'ACORCH',
   'CCORCH',
   'STRING',
)

# Regular expression rules for simple tokens
t_DSPTS   = r'\:'
t_COMA  = r'\,'
t_ACORCH  = r'\['
t_CCORCH  = r'\]'

#expresion regular de cadenas String
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value =  t.value[1:-1]
    return t 

# expresion regular de numeros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# expresion regular de una variable
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


