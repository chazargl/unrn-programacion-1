productos = []
cantidad = 0
comienzo = True

while comienzo :
    producto = input("Ingrese un producto o 'fin' para terminar ")
    if producto == 'fin' :
        print('Se ingreso fin\n')
        break
    else :
        productos.append(producto)
        cantidad = cantidad + 1

if cantidad != 0 :
    print(f'La cantidad de productos fue: {cantidad}')
    print(f'El primer producto fue: {productos[0]}')
    print(f'El ultimo producto fue: {productos[-1]}')
else:
    print(f'La cantidad de productos fue: {cantidad}. No se ingresaron productos')