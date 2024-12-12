#Suma de los dígitos de un número: 
# Recorre cada dígito de un número (convirtiéndolo en una cadena de texto) y suma sus valores utilizando un ciclo for.

numero = input("Ingresa un número: ")

suma_digitos = 0

for digito in numero:
    suma_digitos += int(digito)
print(f"La suma de los dígitos de {numero} es {suma_digitos}")