registro_temperatura = [
    'FREY;12',
    'OTTO;8°C',
    'CATEDRAL;8',
    'FREY;5'
]

total = 0

for registro in registro_temperatura:
    if registro.count(';') != 1:
        print('Hay un error en los datos ingresados ',registro, ' reintentar.')
        continue

    nombre, temperatura = registro.split(';')

    if temperatura.isnumeric():
            total += int(temperatura)

print(total)
