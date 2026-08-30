def sumador(anterior, siguiente):
    if siguiente < anterior:
        raise ValueError('El numero siguiente no puede ser mas chico que el anterior')
    else:
        return siguiente + anterior

anterior = 0
while True:
    print(f'El numero anterior es {anterior_n}')
    siguiente_n = int(input('Ingrese el siguiente numero: '))
    sumador(anterior_n, siguiente_n)
    anterior_n = siguiente_n