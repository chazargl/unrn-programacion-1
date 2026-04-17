nums = [1, 100, 300, 1000]
suma = 0
for i in nums:
    suma = suma + i

print(f'La suma total de los elementos de la lista es: {suma}')
print(f'La cantidad de elementos es: {len(nums)}')
print(f'El promedio es: {(suma/len(nums))}')


