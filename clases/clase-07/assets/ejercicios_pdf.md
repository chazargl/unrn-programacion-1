# Ejercicios PDF

## Ejercicio 0: Teoría Full

1. Explica con tus palabras qué hace `if`, `elif` y `else`. ¿En qué caso usarías cada uno?

> If, elif, else: Evaluan condiciones para que se ejecute un bloque de codigo. Si se cumplen las condiciones, la expresion se evalua como `True` (verdadera) y se ejecuta el bloque de codigo dentro de esa sentencia. De lo contrario si se evalua como `False` (falso), se ignora todo ese bloque de codigo. Usaria `if` para evaluar una condicion (o varias acompañado por `and` o `or`) particular; luego para todos los demas casos que no estan contemplados por el `if` utilizaria `else`. En una situacion `if` - `else` se ejecutara una de las dos acciones posibles, si cumple la condicion se ejecuta el bloque de codigo del `if`, para todos los otros casos que no la cumplan se ejecuta el bloque de codigo del `else`. Si necesitamos ejecutar diferentes bloques de codigo para diferentes situaciones usaria `if` independientes. Por otro lado para que se ejecute un solo bloque de codigo dependiendo de cada evaluacion usaria `if` - `elif` - `else`.

2. Explica con tus palabras qué hace `while` y en qué se diferencia de un `for`. ¿En qué caso usarías cada uno?

> `while` es una iteracion, esto significa que el bloque de codigo dependiente se seguira ejecutando mientras la condicion evaluada siga siendo `True`. En el caso del `for` tambien es una iteracion, pero para una candtidad predefinida de veces.

## Ejercicio 1

```python
def sumar(lista):
total = 0
for n in lista:
total += n
print(total)
```

Pregunta: ¿Cumple si la consigna pide devolver? ¿Por qué?
> En este caso no se cumple la consigna de devolver, ya que esta mostrando a traves de pantalla con la instruccion print el total. Para que se cumpla la consigna deberia utilizarse en la funcion la instruccion return.

## Ejercicio 2

Consigna: Imprimir el ultimo numero.

```python
numeros = [1, 2, 3]
print(numeros[3])
```

Pregunta: ¿Qué ocurre si ejecutamos este codigo ? ¿Cambiarias algo?

> Al ejecutar el codigo anterior el programa indicara un error fuera de rango. Para imprimir el ultimo numero de una lista es conveniente la utilizacion de el acceso por indice negativo `[-1]` Que se adapta a cualquier cantidad de elementos dentro de una lista.

## Ejercicio 3

A partir de la siguiente lista: `numeros = [-1, 1, -2, -3, 7, 10]`

Mostrar:

- Cuántos números son positivos
- Cuántos son negativos
- La suma total (NO USAR `SUM()`.)

Pistas:

- Usar for
- Definir variable numeros_positivos y
numeros_negativos.
- Usar IFs.

[Resolucion Ej.3](../scripts/ej3.py)

## Ejercicio 4

Crear una función que reciba una lista de números y devuelva la suma de los números pares.

Utilizar la siguiente lista para llamar a la función: `numeros = [2, 4, 5, 7, 9, 10, 12]`

Llamar a la función y mostrar el resultado.

Pistas:

- Definir una función con argumentos
- Se puede usar `SUM()`

[Resolucion Ej.4](../scripts/ej4.py)

## Ejercicio 5

Crear una función que reciba una lista de números y devuelva la suma de los números pares. Solicitar 5 numeros al usuarios, llamar a la función y mostrar el resultado.

Pistas:

- Definir una función con argumentos
- Se puede usar `SUM()`
- Usar `while` o `for i in range()`...

[Resolucion Ej.5](../scripts/ej5.py)

## Ejercicio 6

Pedir números al usuario hasta que ingrese 0. Guardar en una lista.

Luego:

- Mostrar cuántos números son positivos
- Mostrar cuántos son negativos
- Mostrar la suma total (NO USAR `SUM()`.)

Pistas:

- Usar `while`
- Definir variable numeros_positivos y numeros_negativos.
- Usar `if`.

[Resolucion Ej.6](../scripts/ej6.py)

## Ejercicio 7 ( NO ENTRA EN EL EXAMEN )

Crear una función que:

- Reciba una lista de números
- Devuelva una lista con el número mayor y cuántas veces aparece.
- No usar `max()` ni `count()`

Llamar a la función con la siguiente lista:
`numeros = [4, 9, 1, 9, 3]`

Pistas:

- Usar for
- Usar IFs
- Crear variables contadoras

[Resolucion Ej.7](../scripts/ej7.py)

## Ejercicio 8

Crear una función que:

- Reciba una lista de números
- Devuelva una lista con el número menor y cuántas veces aparece.
- No usar min() ni count()

Llamar a la función con la siguiente lista: `numeros = [-4, -9, 1, -9, 3]`

Pistas:

- Usar `for`
- Usar `ifF`
- Crear variables contadoras

[Resolucion Ej.8](../scripts/ej8.py)