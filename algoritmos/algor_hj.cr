notas = {"Ana" => 15, "Luis" => 9}
contador = 0
aprobados = 0

while contador < 2 do
  aprobados = aprobados + 1
end

until aprobados >= 2 do
  aprobados = aprobados + 1
end

puts aprobados

def calcular(nota = 10)
  resultado = nota + 1
end