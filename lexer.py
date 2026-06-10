import ply.lex as lex

tokens = (
    'ID',
    'INT',
    'STRING',

    'ASSIGN', 
    'HASH_ARROW',     
    'COLON',       
    'PLUS',
    'MINUS',

    'WHILE',
    'UNTIL',
    'DEF',
    'END',

    'LPAREN',
    'RPAREN',
    'COMMA',

    'TYPE',
)


#Aporte Hailie Jimenez

reserved = {
    'while': 'WHILE',
    'until': 'UNTIL',
    'def': 'DEF',
    'end': 'END',
}

t_COLON= r':'
t_ASSIGN= r'='
t_HASH_ARROW =r'=>'
t_PLUS= r'\+'
t_MINUS= r'\-'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
    
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
#FIN APORTE HAILIE JIMENEZ

lexer = lex.lex()