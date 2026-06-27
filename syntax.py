import ply.yacc as yacc
from lexer import tokens, lexer

#aporte hailie jimenez
errores=[]
semantic_errors = []
symbol_table = {}

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
    pass

def p_parameter(p):
    '''
    parameter : ID
              | ID ASSIGN value
              | MULTIPLY ID
    '''
                # Se agregó MULTIPLY ID para el splat *args (Aporte Christian Macias)

    #Aporte Hailie Jimenez
    if len(p) == 4:  # ID ASSIGN value
        if isinstance(p[3], dict):
            symbol_table[p[1]] = p[3]["type"]
        p[0] = {"name": p[1], "type": symbol_table.get(p[1], "Unknown")}
    elif len(p) == 2:  # ID solo
        symbol_table[p[1]] = "Unknown"
        p[0] = {"name": p[1], "type": "Unknown"}
    else:  # MULTIPLY ID
        symbol_table[p[2]] = "Unknown"
        p[0] = {"name": p[2], "type": "Unknown"}

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
    
    #regla semantica 3 Hailie Jimenez

    if len(p) == 4:
        var_name = p[1]
        expr = p[3]
        if isinstance(expr, dict):
            symbol_table[var_name] = expr["type"]
        p[0] = {
            "node": "assignation",
            "name": var_name,
            "value": expr
        }

    elif len(p) == 6:
        var_name = p[1]
        declared_type = p[3]
        expr = p[5]

        if isinstance(expr, dict):
            expr_type = expr["type"]

            # - inicio aporte christian macias -
            # soporte para union types en verificación de tipo de asignación
            if isinstance(declared_type, str) and '|' in declared_type:
                _allowed = [t.strip() for t in declared_type.split('|')]
            else:
                _allowed = [declared_type]
            # - fin aporte christian macias -

            if expr_type not in _allowed and expr_type not in ("Error", "Unknown"):
                semantic_errors.append(
                    f"Error semántico [línea {p.lineno(1)}]: no se puede asignar un valor de tipo "
                    f"'{expr_type}' a una variable de tipo '{declared_type}'."
                )

            symbol_table[var_name] = declared_type

    
        p[0] = {
            "node": "typed_assignation",
            "name": var_name,
            "declared_type": declared_type,
            "value": expr
        }
    # print(f"[DEBUG assignation] {p[1]} = {p[3]} → symbol_table ahora: {symbol_table}")

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
    p[0] = p[1] #hailie jimenez
    
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
    #regla semantica 4 Hailie Jimenez
    if len(p) == 4:
        left = p[1]
        operator = p[2]
        right = p[3]

        # print(f"[DEBUG expression] {left} {operator} {right} → ", end="")

        arithmetic_operators = ["+", "-", "*", "/"]
        numeric_types = ["Int32", "Float64"]

        if operator in arithmetic_operators:
            left_type = left["type"] if isinstance(left, dict) else "Unknown"
            right_type = right["type"] if isinstance(right, dict) else "Unknown"

            # Si alguno es Unknown, no podemos validar — lo dejamos pasar sin error
            if left_type == "Unknown" or right_type == "Unknown":
                p[0] = {"type": "Unknown", "value": None}
            elif left_type not in numeric_types or right_type not in numeric_types:
                semantic_errors.append(
                    f"Error semántico [línea {p.lineno(2)}]: operación '{operator}' no permitida "
                    f"entre tipos '{left_type}' y '{right_type}'."
                )
                p[0] = {"type": "Error", "value": None}
            else:
                result_type = "Float64" if "Float64" in (left_type, right_type) else "Int32"
                p[0] = {"type": result_type, "value": None}

        else:
            p[0] = {
                "type": "Bool",
                "value": None
            }

    elif len(p) == 2:
        p[0] = p[1]

    # Caso: NOT expression
    elif len(p) == 3:
        expr = p[2]

        if isinstance(expr, dict) and expr["type"] != "Bool":
            semantic_errors.append(
                f"Error semántico [línea {p.lineno(1)}]: operador '!' no permitido "
                f"con tipo '{expr['type']}'."
            )

            p[0] = {
                "type": "Error",
                "value": None
            }
        else:
            p[0] = {
                "type": "Bool",
                "value": None
            }


def p_condition(p):
    '''
    condition : expression
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

    #rhailie jimenez
    token_type = p.slice[1].type
    value = p[1]
    # print(f"[DEBUG value] token={p.slice[1].type} valor={p[1]} → {p[0]}")
    if token_type == "INT":
        p[0] = {
            "type": "Int32",
            "value": value
        }

    elif token_type == "FLOAT":
        p[0] = {
            "type": "Float64",
            "value": value
        }

    elif token_type == "STRING":
        p[0] = {
            "type": "String",
            "value": value
        }

    elif token_type == "BOOLEAN":
        p[0] = {
            "type": "Bool",
            "value": value
        }

    elif token_type == "ID":
        var_name = value

        if var_name in symbol_table:
            p[0] = {
                "type": symbol_table[var_name],
                "value": var_name
            }
        else:
            # - inicio aporte christian macias -
            # Regla Semántica 1: Uso de variable no declarada
            if var_name not in builtin_functions:
                semantic_errors.append(
                    f"Error semántico [línea {p.lineno(1)}]: la variable '{var_name}' no ha sido declarada en el ámbito actual."
                )
            # - fin aporte christian macias -
            p[0] = {
                "type": "Unknown",
                "value": var_name
            }

    elif token_type == "hash":
        p[0] = {
            "type": "Hash",
            "value": value
        }

    elif token_type == "array":
        p[0] = {
            "type": "Array",
            "value": value
        }

    else:
        p[0] = {
            "type": "Unknown",
            "value": value
        }

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

# Variables globales para las reglas semánticas
constants_set = set()  # registra constantes declaradas (Regla Semántica 2)
builtin_functions = {'puts', 'print', 'gets', 'p', 'pp', 'raise', 'exit', 'rand', 'chomp'}

# Variables: Constantes y Union Types

# Regla Semántica 2: Redeclaración de constante
def p_const_assignation(p):
    '''
    const_assignation : CONST ASSIGN expression
    '''
    const_name = p[1]
    if const_name in constants_set:
        semantic_errors.append(
            f"Error semántico [línea {p.lineno(1)}]: la constante '{const_name}' no puede ser reasignada."
        )
    else:
        constants_set.add(const_name)
        if isinstance(p[3], dict):
            symbol_table[const_name] = p[3].get("type", "Unknown")
        else:
            symbol_table[const_name] = "Unknown"
    p[0] = {"node": "const_assignation", "name": const_name}

def p_type_union(p):
    '''
    type_union : TYPE PIPE TYPE
               | type_union PIPE TYPE
    '''
    p[0] = f"{p[1]} | {p[3]}"

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

# Ingreso de datos por teclado: encadenamiento de métodos (gets.chomp, gets.chomp.to_i, gets.chomp.to_f)
def p_value_method_chain(p):
    '''
    value : value DOT ID
    '''
    method = p[3]
    if method == 'to_i':
        p[0] = {"type": "Int32", "value": None}
    elif method == 'to_f':
        p[0] = {"type": "Float64", "value": None}
    else:
        p[0] = {"type": "String", "value": None}

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