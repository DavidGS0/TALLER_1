# Suma de una serie geométrica: 
# Calcula la suma de los primeros n términos de una serie geométrica utilizando un ciclo for. Multiplica el término inicial por la razón en cada iteración. 

a, r, n = 1, 2, 99
suma = 0
termino = a

for i in range(n):
    suma += termino
    termino *=r
print("suma de la serie geometrica:", suma)