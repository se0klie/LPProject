from datetime import datetime
from lexer import lexer
from syntax import parser, errores, semantic_errors, symbol_table
import os

nombre="hailie_jimenez"
errores=[]
for filename in os.listdir("./algoritmos/"):
    if filename.endswith("hj.cr"):
        with open(f"./algoritmos/{filename}") as f:
            data = f.read()
            parser.parse(data)
    
        timestamp = datetime.now().strftime("%d-%m-%Y-%Hh%M")
        parser.parse(data, lexer=lexer)
        log_name = f"semantico-{nombre}-{timestamp}.txt"
        with open(log_name, "w") as log:

            print("\n=== Tabla de símbolos ===")
            for var, tipo in symbol_table.items():
                print(f"  {var}: {tipo}")

            print("\n=== Errores sintácticos ===")
            for e in errores:
                print(" ", e)

            print("\n=== Errores semánticos ===")
            for e in semantic_errors:
                print(" ", e)
            if errores:
                log.write("Errores sintácticos:\n")
                for error in errores:
                    log.write(error + "\n")

            if semantic_errors:
                log.write("\nErrores semánticos:\n")
                for error in semantic_errors:
                    log.write(error + "\n")

            if not errores and not semantic_errors:
                log.write("Análisis sintáctico y semántico exitoso. No se encontraron errores.\n")
