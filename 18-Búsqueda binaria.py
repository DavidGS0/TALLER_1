# Búsqueda binaria: 
# Divide una lista ordenada en mitades para encontrar un elemento específico utilizando un ciclo while. Este ejercicio utiliza índices y comparación. 

lista = [1, 2, 3, 4, 5]
objetivo = 9
izquierda, derecha = 0, len(lista) - 1
encontrado = False
while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        encontrado = True
        break
    elif lista[medio] < objetivo:
        izquierda = medio + 1
    else:
        derecha = medio - 1
print(f"el numero {objetivo} fue encontrado? {encontrado}")