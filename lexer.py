import ply.lex as lex

tokens = (
    'ID',
    'INT',
    'BOOLEAN',
    'FLOAT',
    'STRING',

    'ASSIGN',
    'HASHROCKET',
    'COLON',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',

    'WHILE',
    'UNTIL',
    'DO',
    'DEF',
    'END',

    'LPAREN',
    'RPAREN',
    'COMMA',

    'TYPE',

    # ----- Tokens aporte Christian Macias -----
    'CONST',
    'PIPE',
    'CASE',
    'WHEN',
    'ELSE',
    'LBRACE',
    'RBRACE',
    'STAR',
    'DSTAR',
    'DOT',        # acceso a métodos: gets.chomp, gets.chomp.to_i, etc.

    # ----- Tokens aporte Paulo Tapia -----
    'INSTANCE_VAR',
    'CLASS_VAR',
    'LBRACKET',
    'RBRACKET',
    'AND',
    'OR',
    'NOT',
    'SYMBOL', 

    'LT',
    'LE',
    'GT',
    'GE',     
    
    'IF',
    'ELSIF',
    'RETURN',
)


#Aporte Hailie Jimenez
# Variables: type inference  ·  Control: while-do/until
# Datos: hash              ·  Funcion: params

reserved = {
    'while': 'WHILE',
    'until': 'UNTIL',
    'do': 'DO',
    'def': 'DEF',
    'end': 'END',
    'true': 'BOOLEAN',
    'false': 'BOOLEAN',

#Estructuras if/elseif y return (Aporte Paulo Tapia)
    'if': 'IF',
    'elsif': 'ELSIF',
    'return': 'RETURN',
#Fin Aporte Paulo Tapia

# Tipos de datos para type inference / control structures (Aporte Christian Macias)
    'Int32': 'TYPE',
    'Int64': 'TYPE',
    'Float32': 'TYPE',
    'Float64': 'TYPE',
    'String': 'TYPE',
    'Bool': 'TYPE',
    'Char': 'TYPE',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'else': 'ELSE'
# Fin aporte Christian Macias
    
}

t_COLON= r':'
t_ASSIGN= r'='
t_HASHROCKET =r'=>'
t_PLUS= r'\+'
t_MINUS= r'\-'
t_MULTIPLY= r'\*'
t_DIVIDE= r'\/'


def t_FLOAT(t):
    r'[0-9]+.[0-9]+'
    return t

# -------------- inicio aporte Christian Macias --------------
# Fix de jerarquia para constantes
def t_CONST(t):
    r'[A-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'CONST')
    return t
#-----fin aporte Christian Macias-----

#added to recognize reserved words automatically without defining a rule for each
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t
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
t_DOT    = r'\.'        # punto para encadenamiento de métodos (gets.chomp)


# --- Cadenas  ---
def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

# --- Comentarios ---
def t_COMMENT(t):
    r'\#.*'
    pass

#FIN APORTE CHRISTIAN MACIAS

# Inicio Aporte Paulo Tapia

# Arrays
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Operadores logicos
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Operadores relacionales
t_LE = r'<='
t_GE = r'>='
t_LT = r'<'
t_GT = r'>'

# Variables de instancia y clase
def t_CLASS_VAR(t):
    r'@@[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_INSTANCE_VAR(t):
    r'@[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Simbolos
def t_SYMBOL(t):
    r':[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Fin aporte Paulo Tapia

#Aporte Hailie Jimenez
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
