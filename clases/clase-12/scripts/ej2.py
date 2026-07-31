# Dada la siguiente lista de tuplas:
mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

# Escribí un programa que:

# 1. Cree un diccionario donde la clave sea la ubicación.
# 2. Cada ubicación debe guardar una lista con sus mediciones.
# 3. Cree un conjunto con todos los tipos de medición sin repetir.
# 4. Muestre el diccionario final.
# 5. Muestre el conjunto de tipos encontrados.

ubicacion = {} # Creacion de diccionario de ubicaciones.

for tipo, valor, lugar in mediciones : # Desempaquetado de tuplas.
    if lugar in ubicacion : # Condicional para la ubicacion, si existe agrega el valor.
        ubicacion[lugar].append(valor)
    else : # Si no existe crea la lista con el valor.
        ubicacion[lugar] = [valor]


tipo_medicion = set() # Inicalizacion de conjunto vacio.
for tipo, valor, lugar in mediciones : # Desempaquetado de tuplas.
    tipo_medicion.add(tipo) # Agrego el tipo al conjunto.

print(ubicacion) # Muestra el diccionario.
print(tipo_medicion) # Muestra el conjunto.