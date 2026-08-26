import sys

archivo = sys.argv[1]
posicion = int(sys.argv[2]) -1
palabras = None

with open(ruta_archivo, 'r') as archivo:
    palabras = archivo.readline().split(' ')

print(palabras[posicion])