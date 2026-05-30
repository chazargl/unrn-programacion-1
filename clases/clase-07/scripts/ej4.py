# Ejercicio 4

# Crear una función que reciba una lista de números y devuelva la suma de los números pares.
# Utilizar la siguiente lista para llamar a la función: `numeros = [2, 4, 5, 7, 9, 10, 12]`
# Llamar a la función y mostrar el resultado.

# Pistas:
# - Definir una función con argumentos
# - Se puede usar `SUM()`

def pares (numeros):
    return sum(num for num in numeros if num % 2 == 0)

numeros = [2, 4, 5, 7, 9, 10, 12]
resultado = pares(numeros)
print(f'La suma de los pares es: {resultado}')