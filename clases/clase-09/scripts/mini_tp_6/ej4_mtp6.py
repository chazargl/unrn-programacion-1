# La estructura de datos designada fue una lista de diccionario, donde notas es a su vez
# otra lista. Necesitamos recorrer el diccionario buscando el promedio de notas. Eso lo 
# resolveria con un iterador FOR para el recorrido de la lista de estudiantes. Utilizo 
# la funcion suma para sumar el contenido de la lista notas y lo divido por la funcion 
# len que me devuelve la cantidad de notas. Ya con el promedio obtenido utilizo el recorrido 
# para clasificar a los estudiantes segun su promedio, utilizando un condicional IF para las 
# diferentes condiciones a evaluar. Cada clasificacion Promociona, Regulariza y Recursa
# la guardo en una lista para operar mas tarde si fuera necesario, como es el caso de 
# estudiantes en riesgo que solicita convertirla en un set. Usaria un bloque diferente
# dentro del mismo recorrido y el promedio calculado para guardarlo segun la comision
# a la que pertenece a traves de otro IF. Por ultimo calcularia el promedio por comision
# en dos variables diferentes, para poder compararlas luego. Se muestra la informacion
# solicitada y se genera el set desde la lista recursa.



estudiantes = [
    {'nombre': 'Ana', 'notas': [7, 8, 6], 'asistencias': 9, 'comision': 'C1'},
    {'nombre': 'Luis', 'notas': [4, 5, 3], 'asistencias': 6, 'comision': 'C1'},
    {'nombre': 'Mora', 'notas': [9, 8, 10], 'asistencias': 10, 'comision': 'C2'},
    {'nombre': 'Pedro', 'notas': [2, 4, 3], 'asistencias': 7, 'comision': 'C2'}
]

promedio = 0
promociona = []
regulariza = []
recursa = []
notas_com1 = []
notas_com2 = []

for estudiante in estudiantes :
    promedio = round(sum(estudiante['notas']) / len(estudiante['notas'])) # Calculo el promedio.
    print(f'Estudiante: {estudiante['nombre']} - Promedio: {promedio}') # Mostrar el promedio de cada estudiante.

    if promedio >= 8 and estudiante['asistencias'] >= 8 : # Bloque IF de clasificacion de estudiantes.
        promociona.append(estudiante['nombre'])
    elif promedio >= 4 and estudiante['asistencias'] >= 6 :
        regulariza.append(estudiante['nombre'])
    else :
        recursa.append(estudiante['nombre'])
        
    if estudiante['comision'] == 'C1' : # Bloque que guarda notas de cada comision.
        notas_com1.append(promedio)
    else:
        notas_com2.append(promedio)
    
promedio_C1 = sum(notas_com1) / len(notas_com1) # Calculo de promedio por comision.
promedio_C2 = sum(notas_com2) / len(notas_com2)

print(f'\nLa cantidad de estudiantes que promocionan son: {len(promociona)}, los que regularizan: {len(regulariza)} y recursan: {len(recursa)}.')

if promedio_C1 > promedio_C2 : # Bloque de mostrar la comision con mejor promedio general. Esta solucion me genera dudas, ya que si bien cumple con lo solicitado
    print(f'La comision 1 fue la de mayor promedio con un resultado de: {promedio_C1}.') # me gustaria que la resolucion se adapte a cualquier cantidad de comisiones.
elif promedio_C2 > promedio_C1 : 
    print(f'La comision 2 fue la de mayor promedio con un resultado de: {promedio_C2}.')
else :
    print(f'Ambas comisiones resultaron con el mismo promedio de notas: {promedio_C1}.')

en_riesgo = set(recursa) # Generacion de set de estudiantes en riesgo.
print(f'Los estudiantes en riesgo son: {en_riesgo}')