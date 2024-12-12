# Verificación de número primo: 
# Usa un ciclo for para verificar si un número es divisible por algún número entre 2 y su raíz cuadrada. Si no tiene divisores, es primo. 

numero = int(input("Ingresa un número: "))

if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    raiz_cuadrada = numero ** 0.5
    print(f"La raíz cuadrada de {numero} es {raiz_cuadrada:.2f}")

    tiene_divisores = False

    limite = int(raiz_cuadrada) + 1
    for i in range(2, limite):
        if numero % i == 0:  
            tiene_divisores = True
            print(f"{numero} es divisible por {i}, por lo tanto es numero par.")
            break
    if not tiene_divisores:
        print(f"{numero} por lo tanto es número primo.")