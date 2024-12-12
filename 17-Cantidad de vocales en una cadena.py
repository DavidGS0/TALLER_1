# Cantidad de vocales en una cadena: 
# Recorre cada carácter de una cadena de texto con un ciclo for y cuenta cuántos de ellos son vocales.

cadena = input("Ingresa una cadena de texto: ")

vocales = "aeiouAEIOU"

contador_vocales = 0

for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1

print(f"La cantidad de vocales en la cadena es: {contador_vocales}")