materia = ('Programacion 1', 3, 'Miercoles')

print(materia[0])
print(materia[1])
print(materia[2])

nombre, comision, dia = materia #desempaquetado de tupla
print(f'La materia es: {nombre}')
print(f'Pertenece a la comision: {comision}')
print(f'Se cursa los dias: {dia}')