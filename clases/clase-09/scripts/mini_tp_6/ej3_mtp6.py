libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]


generos_disponibles = set() # Creacion de set para generos.
cantidad_por_genero = {} # Creacion de diccionario para la cantidad de libros por genero.
maximo = -1 

for titulo, _, anio, genero in libros : # Desempaquetado de tupla, ignorando autor ya que no se usa en el ejercicio.
    if anio > 2010 :
        print(f'Titulo: "{titulo}" publicado despues del 2010.') # Mostrar todos los títulos publicados después de 2010.

    if genero not in generos_disponibles : # Obteniendo un set con los géneros disponibles.
        generos_disponibles.add(genero) # Agrega el generos al set.
        cantidad_por_genero[genero] = 1 # Cuenta si es la primera aparicion. Diccionario.
    else:
        cantidad_por_genero[genero] += 1 # suma 1 si ya aparecio.

print('\n') # Solamente estetico.

for num in cantidad_por_genero.values() : # Recorro el diccionario solo para los valores.
    if num > maximo :
        maximo = num # Guardo la maxima cantidad de libros por genero.
for gen, num in cantidad_por_genero.items() :
    if num == maximo : # Imprimo todos los generos que sean iguales al maximo.
        print(f'El genero que tiene mas libros es: {gen}, con {num} unidades.')


print(f'\nLa cantidad de libros por genero es: {cantidad_por_genero}.\n') # No se pide la muestra pero es utilizada para control.
    
print(f'Los generos sin repetirse son: {', '.join(generos_disponibles)}.')