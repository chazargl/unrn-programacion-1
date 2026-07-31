# 2. Mediante comprensión devolve una lista que devuelva True para los aprobados 
# (mayor o igual a 6) o False para los desaprobados.

notas = [2, 4, 6, 8, 10, 3, 7, 9]

aprobados = ['True' if x >= 6 else 'False' for x in notas]
print(aprobados)