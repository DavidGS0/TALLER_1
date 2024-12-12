# Potencia de un número:
#  Calcula la potencia de un número multiplicando la base por sí misma tantas veces como indique el exponente, utilizando un ciclo for.

base = int(input("ingresa el numero que quieres elevar: "))
exponente = int(input('ingresa la potencia a elevar: '))
resultado = 1
for i in range(exponente):
    resultado *= base
print(base, "^", exponente, "=", resultado)