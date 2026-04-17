def saludo() :
    print(f'Bienvenido a mi programa\n')

saludo()

def devolver_saludo() :
    return 'Este saludo es la devolucion de la funcion\n'

devolver = devolver_saludo()
print(devolver)

def saludo_personalizado(usuario = 'amigo') :
    return f'Que gusto volver a verte {usuario}!'

usuario = input('Hola ingresa tu nombre ')
if usuario == '' :
    print(saludo_personalizado())
else :
    print(saludo_personalizado(usuario))





