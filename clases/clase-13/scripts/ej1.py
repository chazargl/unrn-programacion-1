# 1. Mediante comprensión normaliza los textos  de la siguiente lista:

comandos = [" ENCENDER ", "apagar", " Estado ", "REINICIAR", " salir "]

cmd_normalizados = [x.title().split() for x in comandos]
print(cmd_normalizados)