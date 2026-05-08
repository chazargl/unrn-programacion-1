# Mini TP 5 - Teoría y ejercicios básicos

## Objetivo

Reforzar los conceptos base de tuplas, conjuntos y diccionarios con ejercicios cortos y directos.

## Parte 1 - Teoría

Responder en un archivo de texto plano, con tus palabras, en no más de 4 líneas por punto:

1. ¿Qué es una **tupla** y en qué se diferencia de una lista?
2. ¿Qué es un **conjunto (set)** y qué problema resuelve mejor que una lista?
3. ¿Qué es un **diccionario** y cuándo conviene usar clave-valor?
4. ¿Qué significa combinar estructuras de datos? Dar un ejemplo simple.

> 1. Las **tuplas** en Python son estructuras de datos ordenadas e inmutables, no se pueden modificar tras su creación. Se definen mediante paréntesis () y comas, permitiendo almacenar colecciones de elementos heterogéneos (diferentes tipos de datos). Son más rápidas y eficientes en memoria que las listas, ideales para proteger datos constantes. En definitiva sería un lista inmutable. Aunque no se puede modificar una tupla, sí se puede asignar un nuevo valor a una variable que representa una tupla.

> 2. Un **conjunto** es una colección en la que cada elemento debe ser único. Al meter una colección de valores con elementos duplicados en set(), Python identifica los elementos únicos de la colección y crea un conjunto con ellos. El resultado es una lista sin repeticiones. Es fácil confundir conjuntos y diccionarios porque ambos usan llaves. Cuando vea llaves, pero no pares clave-valor, lo más probable es que se trate de un conjunto. A diferencia de lo que ocurre con listas y diccionarios, los conjuntos no mantienen los elementos en un orden especifíco. El problema que resuelve mejor que una lista sería cuando necesitamos agrupar los elementos únicos y mostrarlos.

> 3. Un **diccionario** de Python es una colección de pares clave-valor. Cada clave se conecta a un valor y podemos usar una clave para acceder al valor asociado a la misma. El valor de una clave puede ser un número, una cadena, una lista o incluso otro diccionario. En Python, un diccionario va entre llaves ({}), con una serie de pares clave-valor entre ellas. Cada clave se conecta con su valor mediante dos puntos y varios pares clave-valor se separan entre ellos por comas. Los diccionarios son estructuras dinámicas, mutables y ordenadas. Podemos añadirles nuevos pares clave-valor en cualquier momento. Para añadir un nuevo par, daríamos el nombre del diccionario seguido por la nueva clave entre corchetes junto con el nuevo valor. Se utilizan para agrupar información relacionada de forma organizada, como el perfil de un usuario, además de poder crear estructuras mas complejas al incluir otros diccionarios o listas dentro del mismo.

> 4. Combinar estructuras de datos en Python (también conocido como anidamiento o nesting) significa colocar una estructura de datos (como una lista, diccionario, tupla o conjunto) dentro de otra para organizar información compleja y jerárquica. Esto permite modelar situaciones del mundo real que no se pueden representar con una sola lista o diccionario simple. <br>

== Ejemplos: == 
- **Lista de Diccionarios** (Estructura de Tabla o BD). Es la forma más común de representar datos estructurados, como filas en una base de datos.
```
 # Cada diccionario representa un estudiante
estudiantes = [
    {"nombre": "Ana", "nota": 90, "materias": ["Matemáticas", "Historia"]},
    {"nombre": "Luis", "nota": 85, "materias": ["Física", "Arte"]},
    {"nombre": "Carlos", "nota": 92, "materias": ["Química", "Literatura"]}
]
```
 - **Diccionario con Listas** (Agrupamiento de Datos). Útil para agrupar elementos bajo una misma clave o categoría.
```
# Claves son equipos, valores son listas de jugadores
equipos = {
    "RedTeam": ["Juan", "María", "Pedro"],
    "BlueTeam": ["Sofía", "Diego", "Elena"]
}
```
 - **Listas Anidadas** (Matrices o Cuadrículas). Utilizado para representar matrices matemáticas, tableros de juego (como tres en raya) o mapas.
```
# Una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
``` 
 - **Diccionario de Diccionarios** (Estructura Jerárquica). Ideal para representar objetos con múltiples atributos complejos.
```
usuarios = {
    "usuario1": {
        "nombre": "Ana",
        "rol": "admin",
        "detalles": {"id": 101, "email": "ana@mail.com"}
    },
    "usuario2": {
        "nombre": "Bob",
        "rol": "user",
        "detalles": {"id": 102, "email": "bob@mail.com"}
    }
}
```   
 - **Tuplas dentro de Listas** (Registros Inmutables). Útil para listas de datos que no deben cambiar, garantizando integridad.
```
# Lista de coordenadas (x, y)
rutas = [
    (10, 20),
    (30, 40),
    (50, 60)
]
```

## Parte 2 - Ejercicios básicos

### Ejercicio 1 - Tuplas: datos fijos
Crear una tupla `materia = ("Programación 1", 3, "Miércoles")` y resolver:
1. Mostrar el nombre de la materia.
2. Mostrar el número de comisión.
3. Mostrar el día de cursada.
4. Desempaquetar la tupla en tres variables e imprimirlas.

[Resolucion Ej.1](./scripts/mini_tp_5/ej1_mtp5.py)

### Ejercicio 2 - Tuplas: operaciones simples
Dada la tupla:

```python
numeros = (4, 7, 2, 9, 7)
```

Resolver:
1. Mostrar el primer y el último valor.
2. Contar cuántas veces aparece el número `7`.
3. Mostrar el largo de la tupla.

[Resolucion Ej.2](./scripts/mini_tp_5/ej2_mtp5.py)

### Ejercicio 3 - Sets: básicos
Dado:

```python
valores = [3, 3, 5, 7, 5, 8, 8, 8, 10]
```

Resolver:
1. Convertir la lista a set.
2. Mostrar el set resultante.
3. Mostrar cuántos elementos únicos hay.

[Resolucion Ej.3](./scripts/mini_tp_5/ej3_mtp5.py)

### Ejercicio 4 - Sets: pertenencia y altas
Crear un set de materias:

```python
materias = {"Matemática", "Programación"}
```

Resolver:
1. Agregar `"Física"`.
2. Verificar si `"Química"` está en el set.
3. Mostrar el set final.

[Resolucion Ej.4](./scripts/mini_tp_5/ej4_mtp5.py)

### Ejercicio 5 - Diccionarios: ficha simple
Crear un diccionario `alumno` con:
- nombre
- apellido
- edad

Resolver:
1. Mostrar nombre y apellido en una sola línea.
2. Aumentar la edad en 1.
3. Agregar la clave `activo` con valor `True`.
4. Mostrar el diccionario completo.

[Resolucion Ej.5](./scripts/mini_tp_5/ej5_mtp5.py)

### Ejercicio 6 - Diccionarios: recorridos
Dado:

```python
producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}
```

Resolver:
1. Recorrer e imprimir claves.
2. Recorrer e imprimir valores.
3. Recorrer e imprimir `clave: valor`.

[Resolucion Ej.6](./scripts/mini_tp_5/ej6_mtp5.py)
