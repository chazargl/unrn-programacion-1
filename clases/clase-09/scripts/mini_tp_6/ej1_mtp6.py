registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]

# Crea un conjunto y muestra ciudades sin repetir. 
ciudades = set()
for reg in registros :
    ciudades.add(reg[1])

print(ciudades)

# Muestra las fechas disponibles sin repetir.
fechas = set()
for reg in registros :
    fechas.add(reg[0])

print(fechas,'\n')

# Calcular el promedio de temperatura por ciudad (usar diccionario).
registro_temp = {}
mayor_promedio = -99

for ciudad in ciudades : # Utilizo el set ya creado anteriormente para recorrerlo y generar la lista de temperaturas.
    registro_temp[ciudad] = []
    for reg in registros : # Recorro la lista de tuplas para agregar las temperaturas a cada ciudad.
        if ciudad == reg[1] :
            registro_temp[ciudad].append(reg[2])
    promedio = round(sum(registro_temp[ciudad]) / len(registro_temp[ciudad]), 1) # Calculo el promedio y redondeo.
    print(f'El promedio de temperaturas de {ciudad} fue {promedio}')
    if promedio > mayor_promedio : # Guardo el mayor promedio junto con la ciudad.
        mayor_promedio = promedio
        localidad_templada = ciudad
print(f'\nLa ciudad con mayor registro de temperaturas fue: {localidad_templada} con un promedio de {mayor_promedio}°C.')       
print(registro_temp) # Solo utilizado para control de iteraciones, no lo pide el ejercicio.


