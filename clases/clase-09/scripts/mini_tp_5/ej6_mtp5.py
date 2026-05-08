producto = {'nombre': 'mouse', 'precio': 12500, 'stock': 6}

# Recorro e imprimo claves.
for clave in producto.keys() :
    print(clave)
# Resolucion sin el method()
# for clave in producto :
#    print(clave)

# Recorro e imprimo valores.
for valor in producto.values() :
    print(valor)
# Resolucion sin el method()
# for valor in producto :
#    print(producto[valor])

# Recorro e imprimo claves y valores.
for clave, valor in producto.items() :
    print(f'{clave}: {valor}')
