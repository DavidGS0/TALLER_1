# Máximo común divisor (MCD):
# Encuentra el MCD de dos números utilizando el algoritmo de Euclides con un ciclo while, que repite el cálculo del residuo hasta que uno de los números sea cero.

def main():
    while True:
        num1 = int(input("Introduce el primer número (o 0 para salir): "))
        if num1 == 0:
            print("Programa terminado.")
            break
        num2 = int(input("Introduce el segundo número (o 0 para salir): "))
        
        if num2 == 0:
            print("Programa terminado.")
            break
        while num2 != 0:
            residuo = num1 % num2
            print(f"{num1} % {num2} = {residuo}")
            num1, num2 = num2, residuo
        print(f"El Máximo Común Divisor es: {num1}\n")

if __name__ == "__main__":
    main()