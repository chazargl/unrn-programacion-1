ingreso = input("Escriba el producto y su precio separado por ';': ")
try:
    texto, precio = ingreso.split(';')
    
except ValueError:
    print('Producto y precio invalido, ingresar con' \
    'el siguiente formato: "Producto;1200"')

    exit(1)
try:
    precio = float(precio)
    print(f'{texto} cuesta $ {precio}')
except ValueError:
    print('Se ingreso un precio invalido, ' \
    'ingrese valores numericos.')
