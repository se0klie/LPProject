import ply.yacc as yacc
from lexer import tokens

#aporte hailie jimenez
errores=[]
def p_program(p):
    '''
    program : statement_list
    '''

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''

def p_statement(p):
    '''
    statement : assignation
              | expression_statement
              | loop_statement
              | function_definition
              | const_assignation
              | case_statement
              | if_statement
              | return_statement
    '''
                # Se agregaron const_assignation y case_statement (Aporte Christian Macias)
                # Se agregaron if_statement y return_stateement (Aporte Paulo Tapia)
                
def p_function_definition(p):
    '''
    function_definition : DEF ID LPAREN parameters RPAREN statement_list END
    '''

def p_parameters(p):
    '''
    parameters : parameter
               | parameters COMMA parameter
               | empty
    '''

def p_parameter(p):
    '''
    parameter : ID
              | ID ASSIGN value
              | MULTIPLY ID
    '''
                # Se agregó MULTIPLY ID para el splat *args (Aporte Christian Macias)

def p_empty(p):
    'empty :'
    pass

def p_assignation(p):
    '''
    assignation : ID ASSIGN expression 
                | ID COLON TYPE ASSIGN expression
                | ID COLON type_union ASSIGN expression
                | INSTANCE_VAR ASSIGN expression
                | CLASS_VAR ASSIGN expression
    '''
                    # Se agregó la validación para type_union (Aporte Christian Macias)
                    # Se agrego  INSTANCE_VAR y CLASS_VAR (Aporte Paulo Tapia)

def p_operator(p):
    '''
    operator : PLUS
             | MINUS
             | MULTIPLY
             | DIVIDE
             | LT
             | LE
             | GT
             | GE
             | AND
             | OR
            
    '''
    
def p_hash(p):
    '''
    hash : LBRACE hash_pairs RBRACE
    '''

def p_hash_pairs(p):
    '''
    hash_pairs : hash_pair
               | hash_pairs COMMA hash_pair
    '''

def p_hash_pair(p):
    '''
    hash_pair : value HASHROCKET value
    '''

def p_expression_statement(p):
    '''
    expression_statement : expression
    '''
    
def p_expression(p):
    '''
    expression : expression operator expression 
                | value
                | NOT expression

    '''
                # Se agrego NOT expression (Aporte Paulo Tapia)


def p_condition(p):
    '''
    condition : expression
              | NOT expression
    '''


def p_value(p):
    '''
    value : INT 
            | FLOAT 
            | STRING 
            | BOOLEAN
            | ID
            | hash
            | tuple
            | named_tuple
            | array
            | INSTANCE_VAR
            | CLASS_VAR
            | SYMBOL
            | function_call
    '''
                # Se agregaron tuple y named_tuple (Aporte Christian Macias)
                # Se agrego array, INSTANCE_VAR, CLASS_VAR, SYMBOL y function_call

def p_loop_statement(p):
    '''
    loop_statement : while_loop 
                    | until_loop
    '''
def p_while_loop(p):
    '''
    while_loop : WHILE condition DO loop_body END
    '''

def p_until_loop(p):
    '''
    until_loop : UNTIL condition DO loop_body END
    '''

def p_loop_body(p):
    '''
    loop_body : statement 
    '''

def p_error(p):
    if p:
        mensaje = (
            f"Error de sintaxis en línea {p.lineno}: "
            f"token inesperado '{p.value}' "
            f"(tipo {p.type})"
        )
    else:
        mensaje = "Error de sintaxis: fin inesperado del archivo"

    errores.append(mensaje)

#fin aporte hailie jimenez

# inicio aporte Christian Macias

# Variables: Constantes y Union Types
def p_const_assignation(p):
    '''
    const_assignation : CONST ASSIGN expression
    '''

def p_type_union(p):
    '''
    type_union : TYPE PIPE TYPE
               | type_union PIPE TYPE
    '''

# Control: case / when / else
def p_case_statement(p):
    '''
    case_statement : CASE expression when_list END
                   | CASE expression when_list ELSE statement_list END
    '''

def p_when_list(p):
    '''
    when_list : when_clause
              | when_list when_clause
    '''

def p_when_clause(p):
    '''
    when_clause : WHEN expression statement_list
    '''

# Datos: Tuple y NamedTuple
def p_tuple(p):
    '''
    tuple : LBRACE tuple_elements RBRACE
    '''

def p_tuple_elements(p):
    '''
    tuple_elements : expression
                   | tuple_elements COMMA expression
                   | empty
    '''

def p_named_tuple(p):
    '''
    named_tuple : LBRACE named_tuple_pairs RBRACE
    '''

def p_named_tuple_pairs(p):
    '''
    named_tuple_pairs : named_tuple_pair
                      | named_tuple_pairs COMMA named_tuple_pair
    '''

def p_named_tuple_pair(p):
    '''
    named_tuple_pair : ID COLON expression
    '''

# fin aporte Christian Macias

# inicio aporte Paulo Tapia

#Control: if / elsif / else
def p_if_statement(p):
    '''
    if_statement : IF condition statement_list END
                 | IF condition statement_list ELSE statement_list END
                 | IF condition statement_list elsif_list END
                 | IF condition statement_list elsif_list ELSE statement_list END
    '''
 
def p_elsif_list(p):
    '''
    elsif_list : elsif_clause
               | elsif_list elsif_clause
    '''
 
def p_elsif_clause(p):
    '''
    elsif_clause : ELSIF condition statement_list
    '''
 
# Datos: Array
def p_array(p):
    '''
    array : LBRACKET array_elements RBRACKET
    '''
 
def p_array_elements(p):
    '''
    array_elements : expression
                   | array_elements COMMA expression
                   | empty
    '''
 
# Funcion: return y llamada con argumentos
def p_return_statement(p):
    '''
    return_statement : RETURN expression
    '''
 
def p_function_call(p):
    '''
    function_call : ID LPAREN call_arguments RPAREN
    '''
 
def p_call_arguments(p):
    '''
    call_arguments : expression
                   | call_arguments COMMA expression
                   | empty
    '''
 
# fin aporte Paulo Tapia

parser = yacc.yacc(debug=True, write_tables=False)