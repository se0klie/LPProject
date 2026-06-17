from datetime import datetime
from lexer import lexer
from syntax import parser
import os

nombre="nombre_apellido"
for filename in os.listdir("./algoritmos/"):
    if filename.endswith(".cr"):
        with open(f"./algoritmos/{filename}") as f:
            data = f.read()
            parser.parse(data)
    
#         lexer.input(data)

#         timestamp = datetime.now().strftime("%d-%m-%Y-%Hh%M")

#         log_name = f"lexico-{nombre}-{timestamp}.txt"

#         with open(log_name, "w") as log:

#             while True:
#                 tok = lexer.token()

#                 if not tok:
#                     break

#                 log.write(
#                     f"{tok.type} -> {tok.value}\n"
                # ) 


with open("./algoritmos/algor_hj.cr") as f:
    data = f.read()

parser.parse(data)