# Suma de los dígitos de un número con ciclos: 
# Extrae cada dígito de un número utilizando operaciones matemáticas y acumula su suma dentro de un ciclo.

numero = int(input("Ingresa un número entero: "))

suma_digitos = 0

while numero > 0:
    digito = numero % 10
    suma_digitos += digito
    numero //= 10 
print(f"La suma de los dígitos es: {suma_digitos}")