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

    # ----- Tokens aporte Christian Macias (Integrante 3) -----
    'CONST',      
    'PIPE',       
    'CASE',       
    'WHEN',       
    'THEN',       
    'ELSE',       
    'LBRACE',     
    'RBRACE',     
    'STAR',       
    'DSTAR',      
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
#FIN APORTE HAILIE JIMENEZ


#INICIO APORTE CHRISTIAN MACIAS
# Variables: constantes y union types  ·  Control: case/when
# Datos: Tuple/NamedTuple              ·  Funcion: splat *args

# --- Union types y simbolos de Tuple/NamedTuple/splat ---
t_PIPE   = r'\|'        
t_LBRACE = r'\{'        
t_RBRACE = r'\}'
t_COMMA  = r','         
t_LPAREN = r'\('        
t_RPAREN = r'\)'
t_DSTAR  = r'\*\*'      
t_STAR   = r'\*'        

# --- Control: case / when / then / else ---
def t_CASE(t):
    r'case(?![A-Za-z0-9_])'
    return t

def t_WHEN(t):
    r'when(?![A-Za-z0-9_])'
    return t

def t_THEN(t):
    r'then(?![A-Za-z0-9_])'
    return t

def t_ELSE(t):
    r'else(?![A-Za-z0-9_])'
    return t

# --- Variables: constantes y nombres de tipo ---
def t_CONST(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

# --- Cadenas  ---
def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t
#FIN APORTE CHRISTIAN MACIAS


#Aporte Hailie Jimenez
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
