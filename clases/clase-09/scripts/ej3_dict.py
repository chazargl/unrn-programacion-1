materiales_dict = {
    'nombre': 'Martillo',
    'precio': 50,
    'stock': 5
}

print('Producto:', materiales_dict)
materiales_dict['precio'] += materiales_dict['precio'] * 0.1
materiales_dict['stock'] -= 1
print('Producto:',materiales_dict['nombre'], '- Precio actualizado: $',materiales_dict['precio'], '- Stock restante:',materiales_dict['stock'])
