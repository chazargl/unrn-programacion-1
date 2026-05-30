# Ejercicio 6

# Pedir números al usuario hasta que ingrese 0. Guardar en una lista.
# Luego:
# - Mostrar cuántos números son positivos
# - Mostrar cuántos son negativos
# - Mostrar la suma total (NO USAR `SUM()`.)

# Pistas:
# - Usar `while`
# - Definir variable numeros_positivos y numeros_negativos.
# - Usar `if`.

numeros_positivos = 0
numeros_negativos = 0
suma_total = 0
numeros = []

while True :
    num = int(input('Ingrese un numero o 0 para terminar: '))
    if num == 0 :
        print('Se ingreso 0.\n')
        break
    else:
        numeros.append(num)
        print('Se agrego ',num,' a la lista.')
        suma_total += num
        if num > 0 :
            numeros_positivos += 1
        elif num < 0 :
            numeros_negativos += 1

print(f'La cantidad de positivos son: {numeros_positivos}.')
print(f'La cantidad de negativos son: {numeros_negativos}.')
print(f'La suma de los numeros ingresados fue: {suma_total}.')




