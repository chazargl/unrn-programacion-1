# Ejercicio 4 - Edad valida

# Pedir una edad por teclado. Antes de usarla como numero, revisar que el dato tenga
# sentido.

# El programa tiene que aceptar edades numericas entre 0 y 120. Si la persona escribe
# espacios de mas, el programa deberia poder limpiarlos antes de validar.

# Si el dato sirve, mostrar algo como:
# Edad registrada: 25

# Si no sirve, mostrar un mensaje de error claro. No alcanza con que el programa se rompa.

while True:
    edad_ingresada = input('Ingrese una edad entre 0 y 120 años: ')
 
    if edad_ingresada.isnumeric() : # Validacion de solo digitos numericos.
        edad_limpia = int(edad_ingresada.strip()) # Convierte el string a entero sin espacios.
        if 0 <= edad_limpia <= 120 : # Valida los limites.
            print('Edad registrada:', edad_limpia)
            break
    else :
        print('Ingrese un fomato valido para la edad.\n') # Informa que el resultado no es valido e itera.