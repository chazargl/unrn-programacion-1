alumnos = [
    {
        'nombre': 'Joaquin', 
        'notas': [10, 8, 9], 
        'materias': {'Programacion', 'Matematica'}
    },
    {
        'nombre': 'Juan', 
        'notas': [10, 4, 2], 
        'materias': {'Programacion'}   
    },
    {
        'nombre': 'Lucia', 
        'notas': [1, 8, 2], 
        'materias': {'Programacion', 'Ingles'}
    }
]
# print(alumnos)
for alumno in alumnos:
    print(f'Alumno: {alumno['nombre']}') 
for alumno in alumnos:
    suma_notas = 0
    cantidad_notas = 0
    for nota in alumno['notas']:
        suma_notas += nota
        cantidad_notas += 1

    promedio = suma_notas / cantidad_notas

    if promedio >= 4:
        print(alumno['nombre'], "Aprobo", round(promedio,1))
    
for alumno in alumnos:
    if 'Matematica' in alumno['materias']:
        print(alumno['nombre'], 'cursa matematica')

for alumno in alumnos:
    if alumno['nombre'] == 'Joaquin':
        alumno['materias'].add('Laboratorio')
        print(f'Las materias de Joaquin son: {alumno['materias']}')