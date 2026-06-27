# Variables: Constantes
MAX_INTENTOS = 5
VERSION = "2.0"

# Regla Semantica 2: reasignacion de constante (debe generar error)
MAX_INTENTOS = 200

# Variable con union type
codigo_estado : Int32 | String = "Activo"

# Funciones con splat *args y estructuras
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

# Ingreso de datos por teclado
nombre = gets.chomp
edad = gets.chomp.to_i
saldo = gets.chomp.to_f

# Regla Semantica 1: uso de variable no declarada (debe generar error)
resultado = variable_inexistente + 1

# Error sintactico intencional para el log
WHILE
