producto = {'nombre': 'mouse', 'precio': 12500, 'stock': 6}

# Recorro e imprimo claves.
for clave in producto.keys() :
    print(clave)

# Recorro e imprimo valores.
for valor in producto.values() :
    print(valor)


# Recorro e imprimo claves y valores.
for clave, valor in producto.items() :
    print(f'{clave}: {valor}')