VACIO = 0
JUGADOR_1 = 1
JUGADOR_2 = 2

tablero = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

turno_jugador = JUGADOR_1

def imprimir_tablero(tablero):
    # Logica para imprimir tablero (FILITA POR FILITA)
    for linea in tablero :
        print(' | '.join(linea))
        print('----------')

def obtener_posicion():
    # Logica para solicitar datos al usuario (del 1 al 3)
    # Consejo: restar 1 aquí adentro para trabajar con índices 0, 1, 2
    while True :
        fila = input('Por favor ingrese un numero elegir la fila: ')
        columna = input('Por favor ingrese un numero para elegir la columna: ')
        if fila.isnumeric() and columna.isnumeric() :
            fila_ok = int(fila)
            columna_ok = int(columna)
            if (fila_ok <= 3 and fila_ok >= 1) and (columna_ok <= 3 and columna_ok >= 1) :
                fila = fila_ok - 1
                columna = columna_ok - 1
                return fila, columna
                break
        else :
            print('Entrada no valida, verifique si que el valor este entre 1 y 3.')

def validar_posicion(tablero, fila, columna):
    # Logica para validar rango (0 a 2) y posición libre
    if (0 <= fila < 3) == False :
        return False
    if (0 <= columna < 3) == False :
        return False
    if tablero[fila][columna] != '-' :
        return False
    return True

def asignar_posicion(tablero, fila, columna, jugador):
    # Logica para asignar un jugador a una posición
    tablero[fila][columna] = jugador

def imprimir_tablero(tablero):
    # Logica para imprimir tablero (FILITA POR FILITA)
    pass

def buscar_ganador(tablero):
    # Devuelve True si un jugador completó una línea, False si no
    
    pass

def cambiar_turno(turno_jugador):
    # Logica para cambiar de turno
    if turno_jugador == JUGADOR_1
    
imprimir_tablero(tablero) # Mostrar tablero vacío al principio

while True:
    fila, columna = obtener_posicion()
    print(fila, columna)
    if not validar_posicion(tablero, fila, columna):
        print("Posición inválida o ya ocupada. Vuelva a elegir.")
        continue
    
    asignar_posicion(tablero, fila, columna, turno_jugador)
    imprimir_tablero(tablero)

    if buscar_ganador(tablero):
        print(f"¡Ganó el JUGADOR {turno_jugador}!")
        break
        
    turno_jugador = cambiar_turno(turno_jugador)