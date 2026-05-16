def datos (nombre, edad) :
    if edad >= 18:
        return (nombre, edad, True)
    else:
        return (nombre, edad, False)

resultado = datos("Juan Matias", 48)
print(resultado)
    