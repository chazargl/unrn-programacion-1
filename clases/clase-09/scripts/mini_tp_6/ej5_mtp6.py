# En este ejercicio la estructura de datos designada fue una lista de tuplas.
# Para la resolucion definiria un set con los generos para asegurar unicidad.
# Utilizando un iterador WHILE, ya que el ejercicio indica que se debe ingresar
# salir para terminar, y dentro un input que reciba la eleccion. Dentro del
# bloque se analizaria a traves de un condicional IF - ELIF - ELSE cada situacion
# solicitada.

libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("1984", "George Orwell", 1949, "Novela"),
    ("Rayuela", "Julio Cortázar", 1963, "Novela"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Armas, gérmenes y acero", "Jared Diamond", 1997, "Historia"),
    ("Historia mínima de América Latina", "Carlos Malamud", 2014, "Historia"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Cosmos", "Carl Sagan", 1980, "Ciencia"),
    ("Una breve historia del tiempo", "Stephen Hawking", 1988, "Ciencia"),
    ("El arte de la guerra", "Sun Tzu", -500, "Estrategia"),
    ("Pensar rápido, pensar despacio", "Daniel Kahneman", 2011, "Psicologia")
]

generos = set() 

for libro in libros : # Creacion de set de generos unicos.
    generos.add(libro[-1])

print(f'Los generos disponibles para eleccion son: {generos}') # Muestra de generos para eleccion.
while True :
    eleccion = input('\nElija un genero o escriba "salir" para terminar: ').title() # Se utiliza el metodo title para estetica.
    if eleccion == 'Salir' : 
        print('\nSe ingreso salir. Buena lectura. Hasta pronto!.\n')
        break
    elif eleccion in generos : # Evalua si existe el genero.
        for titulo, autor, anio, genero in libros : # Desempaquetado de tupla para comparar y mostrar informacion.
            if eleccion == genero :
                print(f'Tenemos disponible en {genero}: "{titulo}", de {autor}, edicion ({anio}).')
    else :
        print(f'Aun no contamos con libros del genero {eleccion}.\n')        