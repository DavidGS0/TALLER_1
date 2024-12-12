# Área de un triángulo: 
# Calcula el área de un triángulo dada su base y altura con la fórmula (base * altura) / 2. Este ejercicio no requiere un ciclo for. 

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area = calcular_area_triangulo(base, altura)

print(f'El área del triángulo es: {area}')