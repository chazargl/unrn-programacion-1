# Interpretando consignas

## Verificaciones

1. Se pide verificar que un dato es un número?

**RESPUESTA:**

```python
if data.isnumeric() :
    # Codigo La funcion isnumeric no interpreta negativos.
    dato = '-1'
    if dato[0] == '-' :
        dato = dato[1:]
        print(dato)

```

2. Se pide verificar que tiene N cantidad de caracteres?

**RESPUESTA:** 

```python
if len(dato) == 10 :
    # Se valida que el dato tiene 10 caracteres.
```


3. Se pide verificar que no sea un dato vacío?

**RESPUESTA:**

```python
if len(dato) == 0 : 
    # Una forma de resolverlo.

if len(dato) == false :
    # Otra forma de resolverlo.

if dato == '' :
    # Una forma mas de resolverlo.
```


4. Se pide verificar que un elemento más exista más de N veces?

**RESPUESTA:**

```python
datos = 'Nombre, edad, genero'
if datos.count(',') == 2 :
    # Mi codigo.
```


5. Si tenemos que verificar que un texto contenga otro texto?

**RESPUESTA:**

```python
datos = 'Hola mundo'
if 'Hola' in datos :
    # Mi codigo.
```

> Se puede utilizar con cualquier estructura de datos como Diccionarios, Listas, Conjuntos, Tuplas, etc.


## Repeticiones

1. Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?

**RESPUESTA:**

```python
lista = ['1', '2', '3', '4', '5']
for dato in lista :
    if dato.isnumeric() :
        valido = True
        dato_n = int(dato)
    else :
        valido = False
```

2. Hay que pedirle 5 nombres al usuario. ¿Que hacemos?

**RESPUESTA:**

```python
nombres = []
for idx in range(5) :
    nombre = input('Ingrese un nombre: ')
    nombres.append(nombre)
```


3. Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?

**RESPUESTA:**

```python
nombres = []
while True :
    nombre = input('Ingrese un nombre y 'FIN' para finalizar: ')
    if nombre == 'FIN' :
        break
    else :
        nombres.append(nombre)
```


## Archivos

1. Hay que leer un archivo: 

**RESPUESTA:** 

```python
file = open('archivo.txt','r')
contenido = file.read()
# contenido = file.readlines() lee linea a linea '\n' contenido = lista.

```


2. Hay que escribir un archivo:

**RESPUESTA:** 

```python
file = open('archivo.txt','w') # El write pisa todo lo que tenia el archivo si existe.
contenido = file.write('Hola mundo.')
file.close() # Cuando cerramos el archivo, recien ahi el filesystem escribe el archivo.
```


3. ¿Hay que cerrar un archivo?

**RESPUESTA:** 

> Si no se cierra el archivo no se escribe, es decir, no se vuelca el contenido de memoria al archivo.

## Otros
1. Tenemos que solicitarle al usuario que ingrese 25 nombres, apellidos y años de nacimiento. ¿Que hacemos?

```python
datos = []

for idx in range(25) :
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    anio = input('Ingrese su año de nacimiento: ')
    datos.append({
        'nombre': nombre,
        'apellido': apellido,        
        'anio': anio
    })
```


2. Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible.

```python

```