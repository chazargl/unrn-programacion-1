maximo = 0
minimo = 0
comienzo = True

while comienzo :
    numero = int(input('Ingrese un numero o 0 para terminar '))
    if numero == 0 :
        print('Se ingreso el 0\n')
        break
    elif maximo == 0 and minimo == 0 :
        maximo = numero
        minimo = numero
    elif numero > maximo :
        maximo = numero
    elif numero < minimo :
        minimo = numero

print(f'El maximo numero ingresado fue: {maximo}')
print(f'El minimo numero ingresado fue: {minimo}')