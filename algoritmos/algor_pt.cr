# ARRAY CON IF/ELSEIF/ ELSE
 
precios = [10, 25, 8, 40]
stock_minimo = 5
 
descuento = true
promocion = false
 
if descuento && !promocion
  puts "Aplica solo descuento normal"
elsif descuento || promocion
  puts "Aplica alguna rebaja"
else
  puts "Sin rebajas disponibles"
end
 
def calcular_total(cantidad = 1)
  total = cantidad + stock_minimo
  return total
end
 
resultado = calcular_total(3)
 
puts precios
puts resultado