# Cantidad de dígitos de un número:
# Usa un ciclo for para recorrer los caracteres de un número convertido a cadena de texto y cuenta cuántos tiene. 

numero = int(input("Ingresa un número entero: "))

contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero //= 10
        contador += 1  
print(f"La cantidad de dígitos del número es: {contador}")