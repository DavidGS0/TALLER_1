#Suma de los primeros n números naturales: 
# Calcula la suma de los números desde 1 hasta n utilizando un ciclo for. Itera sobre los números en el rango de 1 a n y acumula su suma. 

n = int(input("Introduce un número: "))

suma = 0

for numero in range(1, n + 1):
    suma += numero  
print(f"La suma de los primeros {n} números naturales es: {suma}")