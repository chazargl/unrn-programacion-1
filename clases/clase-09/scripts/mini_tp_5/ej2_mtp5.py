numeros = (4, 7, 2, 9, 7)

print('El primer valor de la tupla es:', numeros[0], '- El ultimo es:', numeros[-1])
contar = 0
for num in numeros :
    if num == 7 :
        contar += 1

print(f'El largo de la tupla es: {len(numeros)}')