# Promedio ponderado: 
# Calcula el promedio ponderado de una lista de calificaciones. Multiplica cada calificación por su peso en un ciclo for y divide entre el total de pesos.

n = int(input("¿Cuántas calificaciones deseas ingresar? "))

calificaciones = []
pesos = []

for i in range(n):
    calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
    peso = float(input(f"Ingresa el peso para la calificación {i + 1}: "))
    calificaciones.append(calificacion)
    pesos.append(peso)

suma_ponderada = 0
suma_pesos = 0

for i in range(n):
    suma_ponderada += calificaciones[i] * pesos[i]
    suma_pesos += pesos[i]

if suma_pesos == 0:
    print("La suma de los pesos es 0. No se puede calcular el promedio ponderado.")
else:
    promedio_ponderado = suma_ponderada / suma_pesos
    print(f"El promedio ponderado es: {promedio_ponderado:.2f}")