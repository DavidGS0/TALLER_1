# Verificar si un número es palíndromo: 
# Usa un ciclo for para comparar los dígitos de un número desde los extremos hacia el centro y verifica si son iguales. 

numero = int(input("ingresa el numero que quieres validar si es palindromo: "))
numero_str = str(numero)
es_palindromo = True
for i in range(len(numero_str) // 2):
    if numero_str[i] != numero_str[-(i+1)]:
        es_palindromo = False
        break
print(f"El numero {numero} es palindromo?: {es_palindromo}")