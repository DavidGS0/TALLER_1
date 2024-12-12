# Media de una lista de números:
# Recorre cada elemento de una lista con un ciclo for, acumula su suma y divide entre el número total de elementos para calcular la media.

entrada = input("Ingresa números enteros separados por comas: ")

numeros = [int(num) for num in entrada.split(",")]

suma = 0
cantidad_elementos = 0

for numero in numeros:
    suma += numero
    cantidad_elementos += 1
media = suma / cantidad_elementos

print(f"La suma de los números es: {suma}")
print(f"La cantidad de elementos es: {cantidad_elementos}")
print(f"La media de los números ingresados es: {media}")