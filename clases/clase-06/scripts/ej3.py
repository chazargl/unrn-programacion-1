x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]

max = 0
min = 0
for i in x :
    if i > max :
        max = i
    elif i < min :
        min = i
print(f'El numero maximo es: {max}')
print(f'El numero minimo es: {min}')