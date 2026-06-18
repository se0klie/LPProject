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
    '''

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
    '''

def p_empty(p):
    'empty :'
    pass

def p_assignation(p):
    '''
    assignation : ID ASSIGN expression 
                | ID COLON TYPE ASSIGN expression
    '''

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
    '''

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
    '''

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



parser = yacc.yacc(debug=True, write_tables=False)

#fin aporte hailie jimenez