sumatoria = 0
contar = -1
comienzo = True

while comienzo :
    numero = int(input('Ingrese un numero o 0 para finalizar '))
    sumatoria = sumatoria + numero
    contar = contar + 1
    if numero == 0 :
        print('Se ingreso 0\n')
        break

print(f'La suma total de numeros ingresados fue: {sumatoria}')
print(f'La cantidad de numeros ingresados fue: {contar}')
print(f'El promedio fue de: {(sumatoria/contar)}')