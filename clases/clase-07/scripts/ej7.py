#  Ejercicio 7 ( NO ENTRA EN EL EXAMEN )

# Crear una función que:
# - Reciba una lista de números
# - Devuelva una lista con el número mayor y cuántas veces aparece.
# - No usar `max()` ni `count()`

# Llamar a la función con la siguiente lista: `numeros = [4, 9, 1, 9, 3]`

# Pistas:
# - Usar for
# - Usar IFs
# - Crear variables contadoras

numeros = [4, 9, 1, 9, 3]

def mayor(numeros_lista):
    mayor = -99999999
    resultado = []
    contador = 0
    for num in numeros_lista:
        if num > mayor:
            mayor = num
    resultado.append(mayor)
    for num in numeros_lista:
        if num == mayor:
            contador += 1
    resultado.append(contador)
    return resultado

print(mayor(numeros))
