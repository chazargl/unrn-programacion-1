comienzo = True
seleccion_usuario = []
while comienzo :
    producto = input('Ingrese su eleccion o "fin" para terminar. ')
    if producto == 'fin' :
        print('\nSe ingreso fin.')
        break
    else :
        seleccion_usuario.append(producto)

def mostrar_productos (seleccion) :
    productos_unicos = []
    for sel in seleccion :
        if sel not in productos_unicos :
            productos_unicos.append(sel)
        cantidad = 0
        while sel in seleccion :
            cantidad = cantidad + 1
        print(f'La cantidad de {sel} elegida fue: {cantidad}')
    print(f'\nLa cantidad de productos ingresados fue: {len(seleccion)}.')
    print(f'\nLos productos elegidos fueron: {productos_unicos}') 

mostrar_productos (seleccion_usuario)