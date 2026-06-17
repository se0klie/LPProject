import ply.yacc as yacc
from lexer import tokens

def p_statement(p):
    '''
    statement : assignation 
                | expression_statement
                | loop_statement
    '''

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
        print(
            f"Error de sintaxis en línea {p.lineno}: "
            f"token inesperado '{p.value}' "
            f"(tipo {p.type})"
        )
    else:
        print("Error de sintaxis: fin inesperado del archivo")


parser = yacc.yacc(debug=True, write_tables=False)

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)