nums = [1, 2, 2, 3, 4, 4, 4, 5]
numeros_unicos = []

for i in nums :
    if i not in numeros_unicos :
        numeros_unicos.append(i)

print(f'La lista de numeros unicos es: {numeros_unicos}')
    