# Ejercicio 5 - Codigo de materia

# Pedir al usuario un codigo de materia con este formato:
# PROG-101

# El programa tiene que validar que:
# - tenga un solo guion `-`;
# - la parte de la izquierda tenga solo letras;
# - la parte de la derecha tenga solo numeros.

# Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo `upper`).

# Ejemplo:
# Codigo valido: PROG-101

# Si no es valido, mostrar un mensaje de error claro.

while True:
    codigo_ingresado = input("Ingrese un codigo de materia, formato admitido 'XXXX-000': ")
    codigo_a_validar = codigo_ingresado.split('-')
    
    for i in range(len(codigo_a_validar)):
        codigo_a_validar[i] = codigo_a_validar[i].strip()
    
    if len(codigo_a_validar) == 2:
        codigo_a_validar[0] = codigo_a_validar[0].upper()
        es_texto_valido = codigo_a_validar[0].isalpha() and len(codigo_a_validar[0]) == 4
        es_num_valido = codigo_a_validar[1].isnumeric() and len(codigo_a_validar[1]) == 3
        if es_texto_valido and es_num_valido:
            print('Codigo validado:','-'.join(codigo_a_validar))
            break
        else:
            print('Error de formato. Debe contener exactamente 4 letras seguidas de 3 números (ej. PROG-101).')
    else:
        print('Formato incorrecto. Debe incluir un único guion separador, y no puede estar vacio. Intente nuevamente.\n')