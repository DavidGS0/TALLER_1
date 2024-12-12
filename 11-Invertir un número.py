# Invertir un número: 
# Recorre los dígitos de un número desde el principio hasta el final utilizando un ciclo for y constrúyelo en orden inverso.

def invertir_numero(numero):

    numero_invertido = 0
    
    while numero > 0:
        digito = numero % 10
        numero_invertido = numero_invertido * 10 + digito
        numero = numero // 10
    return numero_invertido

numero = int(input("Ingresa un número: "))

numero_invertido = invertir_numero(numero)

print(f'El número invertido es: {numero_invertido}')