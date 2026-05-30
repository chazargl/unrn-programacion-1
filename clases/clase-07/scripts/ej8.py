# Ejercicio 8

# Crear una función que:
# - Reciba una lista de números
# - Devuelva una lista con el número menor y cuántas veces aparece.
# - No usar min() ni count()

# Llamar a la función con la siguiente lista: `numeros = [-4, -9, 1, -9, 3]`

# Pistas:
# - Usar `for`
# - Usar `ifF`
# - Crear variables contadoras

numeros = [-4, -9, 1, -9, 3]

def menor(lista_numeros) :
    menor = 99999999
    contador = 0
    resultado = []
    for num in lista_numeros :
        if num < menor :
            menor = num
    resultado.append(menor)
    for num in lista_numeros :
        if num == menor :
            contador += 1
    resultado.append(contador)
    return resultado

print(menor(numeros))