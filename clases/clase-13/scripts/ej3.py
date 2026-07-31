# 3. Transformar en una lista mediante comprensions

mediciones = [3.2, 2.8, 4.1, 5.5, 3.0, 6.2, 4.8]

fuera_de_rango = []
for valor in mediciones:
    if valor < 3.0 or valor > 5.0:
        fuera_de_rango.append(valor)
print(fuera_de_rango)

fuera_de_rango1 = [x for x in mediciones if x < 3.0 or x > 5.0]
print(fuera_de_rango1)