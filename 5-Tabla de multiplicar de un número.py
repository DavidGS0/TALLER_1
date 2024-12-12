# Tabla de multiplicar de un número: 
# Genera la tabla de multiplicar de un número dado del 1 al 10 utilizando un ciclo for. Por cada iteración, calcula el producto y muéstralo.

numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11): 
    producto = numero * i
    print(f"{numero} x {i} = {producto}")