inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}

reposicion = set()
valor_total = 0
for item, datos in inventario.items() : # desempaqueto el primer diccionario para acceder a los datos.
    if datos['stock'] < 5 : # Mostrar productos con bajo stock
        print(f'{item}: Tiene stock bajo, cantidad ({datos['stock']}). Hacer pedido a proveedor.')
        if datos['stock'] <= 2 : # Generar un set con productos que requieren reposición urgente (stock <= 2).
            reposicion.add(item)
    valor_total += datos['precio'] * datos['stock'] # Calcular valor total del inventario (precio * stock por producto).
print(f'\nEl valor total del inventario a fecha es: ${valor_total}.\n')
print(f'Los siguientes articulos necesitan reposicion URGENTE:\n{'\n'.join(reposicion)}.')

