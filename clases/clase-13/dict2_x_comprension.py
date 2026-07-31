productos = {'Teclado': 120, 'Mouse': 80, 'Monitor': 450}

nuevos_precios = {prod: (precio * 0.9 if precio > 100 else precio) for prod, precio in productos.items()}
print(productos)
print(nuevos_precios)