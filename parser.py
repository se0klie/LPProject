from datetime import datetime
from lexer import lexer
from syntax import parser, errores
import os

nombre="nombre_apellido"
errores=[]
for filename in os.listdir("./algoritmos/"):
    if filename.endswith("hj.cr"):
        with open(f"./algoritmos/{filename}") as f:
            data = f.read()
            parser.parse(data)
    
#         lexer.input(data)
        timestamp = datetime.now().strftime("%d-%m-%Y-%Hh%M")
        parser.parse(data, lexer=lexer)
        log_name = f"sintatico-{nombre}-{timestamp}.txt"
        with open(log_name, "w") as log:
            if errores:
                for error in errores:
                    log.write(error + "\n")
            else:
                log.write("Análisis sintáctico exitoso. No se encontraron errores.\n")
#             while True:
#                 tok = lexer.token()
#                 if not tok:
#                     break
#                 log.write(
#                     f"{tok.type} -> {tok.value}\n"
                # ) 