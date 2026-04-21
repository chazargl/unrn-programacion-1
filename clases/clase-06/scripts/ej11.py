def obtener_precio (producto) :
    if producto == 'martillo' :
        return 3000
    elif producto == 'clavos' :
        return 500
    elif producto == 'destornillador' :
        return 1500
    else :
        return 0
    
stock_productos = ['martillo', 'clavos' , 'destornillador']
seleccion_usuario = []
comienzo = True
total = 0

while comienzo :
    eleccion = input('Por favor ingrese su pedido o "fin" para terminar. ')
    if eleccion == 'fin' :
        print('\nSe ingreso fin.')
        break
    else :
        seleccion_usuario.append(eleccion)
        if eleccion in stock_productos :
            print(f'Agregamos {eleccion}\n')
        else :
            print(f'No contamos con stock de {eleccion}. Elija otro producto.\n')

for prod in seleccion_usuario :
        precio = obtener_precio (prod)
        total = total + precio
        
print(f'\nEl precio total de los productos en existencia es ${total}.')



    
    