# Ejercicio 3

# A partir de la siguiente lista: `numeros = [-1, 1, -2, -3, 7, 10]`
# Mostrar:
# - Cuántos números son positivos
# - Cuántos son negativos
# - La suma total (NO USAR `SUM()`.)

# Pistas:
# - Usar for
# - Definir variable numeros_positivos y
# numeros_negativos.
# - Usar IFs.

numeros = [-1, 1, -2, -3, 7, 10]

numeros_positivos = 0
numeros_negativos = 0
suma = 0

for num in numeros :
    if num > 0 :
        numeros_positivos += 1
    elif num < 0 :
        numeros_negativos += 1
    suma += num

print(f'La cantidad de Nº positivos en la lista es: {numeros_positivos}.')
print(f'La cantidad de Nº negativos en la lista es: {numeros_negativos}.')
print(f'La suma total de los elementos de la lista es: {suma}')