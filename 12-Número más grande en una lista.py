# Número más grande en una lista: 
# Compara los números de una lista uno por uno utilizando un ciclo for para encontrar el mayor de ellos.

def Encontrar_numero_mas_grande(lista):
    
    mayor = lista[0]

    for numero in lista:
        if numero > mayor:
            mayor = numero  
    return mayor

entrada = input("Ingresa los números separados por espacio: ")
numeros = [int(item) for item in entrada.split()]
numero_mas_grande = Encontrar_numero_mas_grande(numeros)

print(f'El número más grande en la lista es: {numero_mas_grande}')