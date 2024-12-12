# Factorial de un número dado: 
# Encuentra el factorial de un número multiplicando todos los números desde 1 hasta ese número con un ciclo for. 
# Asegúrate de inicializar la variable acumuladora en 1

n = int(input("Introduce un número: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i 
print(f"El factorial de {n} es: {factorial}")