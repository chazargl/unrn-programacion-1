# Ejercicio 5

# Crear una función que reciba una lista de números y devuelva la suma de los números 
# pares. Solicitar 5 numeros al usuarios, llamar a la función y mostrar el resultado.

# Pistas:
# - Definir una función con argumentos
# - Se puede usar `SUM()`
# - Usar `while` o `for i in range()`...

def pares (numeros):
    return sum(num for num in numeros if num % 2 == 0)

numeros = []
for i in range(5):
    num = int(input(f'[{(i+1)}] Ingrese un numero: '))
    numeros.append(num)

resultado = pares(numeros)
print(f'\nLa suma de los pares es: {resultado}')