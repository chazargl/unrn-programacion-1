## Ejercicio 3 - Acomodar nombres

# Partiendo de esta lista:

# nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]

# Armar una nueva lista llamada `nombres_normalizados` donde cada nombre quede sin
# espacios sobrantes y con un formato prolijo.

# Al final, mostrar la lista. Deberia quedar parecido a esto:
# ["Mara", "Tomas", "Lucia", "Marcos", "Sofia"]

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []

for nom in nombres :
    nombres_normalizados.append(nom.strip().capitalize())
print(nombres_normalizados)