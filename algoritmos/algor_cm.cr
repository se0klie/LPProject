# Variables
MAX_INTENTOS = 5
VERSION = "2.0"

codigo_estado : Int32 | String = "Activo"

# Funciones
def auditar_sistema(*registros)
    coordenadas_red = {192, 168, 1, 10}
    configuracion_servidor = {puerto: 8080, seguro: true}
    
    case codigo_estado
    when "Activo"
        nivel_acceso = 1
    else
        nivel_acceso = 99
    end 
end 

# Error Intencional para el log
WHILE