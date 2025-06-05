# demo_numpy.py

"""
Demo muy sencilla de NumPy.
Este script muestra cómo:
  1) Importar NumPy.
  2) Crear arreglos (arrays) a partir de listas de Python.
  3) Crear arreglos usando funciones como arange(), zeros() y ones().
  4) Realizar operaciones aritméticas básicas elemento a elemento.
  5) Calcular estadísticas básicas (suma, promedio, desviación estándar, mínimo, máximo).
  6) Redimensionar (reshape) un arreglo.
  7) Indexar y rebanar (slicing) arreglos.

Para ejecutarlo:
  1. Asegúrate de tener instalado NumPy:
       pip install numpy
"""

import numpy as np  # Importamos la librería NumPy con alias 'np'

# -------------------------------------------------------------------
# 1) Crear un arreglo (array) a partir de una lista de Python
# -------------------------------------------------------------------
# Supongamos que tenemos una lista de puntajes de un alumno en 4 pruebas:
lista_notas = [75, 82, 78, 85]

# Convertimos la lista en un arreglo de NumPy usando np.array()
arr_notas = np.array(lista_notas)

print("===== Arreglo creado a partir de lista =====")
print(arr_notas)
# Salida esperada:
# [75 82 78 85]

# -------------------------------------------------------------------
# 2) Crear arreglos usando funciones específicas
# -------------------------------------------------------------------
# 2.1) arange(): crea un arreglo con valores en un rango específico
#      Por ejemplo, crear un arreglo de 0 a 9
arr_rango = np.arange(0, 10)  
print("\n===== Arreglo con np.arange(0, 10) =====")
print(arr_rango)
# Salida esperada:
# [0 1 2 3 4 5 6 7 8 9]

# 2.2) zeros(): crea un arreglo lleno de ceros con la forma indicada
#      Por ejemplo, arreglo de 3 filas y 4 columnas con ceros
arr_ceros = np.zeros((3, 4))  
print("\n===== Arreglo de ceros con np.zeros((3, 4)) =====")
print(arr_ceros)
# Salida esperada:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 2.3) ones(): crea un arreglo lleno de unos con la forma indicada
#      Por ejemplo, arreglo de 2 filas y 5 columnas con unos
arr_unos = np.ones((2, 5))
print("\n===== Arreglo de unos con np.ones((2, 5)) =====")
print(arr_unos)
# Salida esperada:
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# -------------------------------------------------------------------
# 3) Operaciones aritméticas básicas elemento a elemento
# -------------------------------------------------------------------
# Tomemos dos arreglos del mismo tamaño:
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 3.1) Suma
suma_ab = a + b
print("\n===== Suma elemento a elemento =====")
print("a:", a)
print("b:", b)
print("a + b =", suma_ab)
# Salida esperada: [11 22 33 44]

# 3.2) Resta
resta_ab = b - a
print("\n===== Resta elemento a elemento =====")
print("b - a =", resta_ab)
# Salida esperada: [9 18 27 36]

# 3.3) Multiplicación
mult_ab = a * b
print("\n===== Multiplicación elemento a elemento =====")
print("a * b =", mult_ab)
# Salida esperada: [10 40 90 160]

# 3.4) División
div_ab = b / a
print("\n===== División elemento a elemento =====")
print("b / a =", div_ab)
# Salida esperada: [10. 10. 10. 10.]

# 3.5) Operaciones con un escalar
#     Por ejemplo, sumar 5 a cada elemento de 'a'
a_mas_cinco = a + 5
print("\n===== Sumar un escalar a cada elemento =====")
print("a + 5 =", a_mas_cinco)
# Salida esperada: [ 6  7  8  9]

# -------------------------------------------------------------------
# 4) Estadísticas básicas sobre un arreglo
# -------------------------------------------------------------------
# Tomemos el arreglo 'arr_notas' que contiene [75, 82, 78, 85]
print("\n===== Estadísticas básicas de arr_notas =====")
print("arr_notas:", arr_notas)

# 4.1) Suma de todos los elementos
suma_notas = arr_notas.sum()
print("Suma de notas:", suma_notas)
# Ejemplo: 75 + 82 + 78 + 85 = 320

# 4.2) Promedio (media) de los elementos
promedio_notas = arr_notas.mean()
print("Promedio de notas:", promedio_notas)
# Ejemplo: 320 / 4 = 80.0

# 4.3) Desviación estándar
desv_notas = arr_notas.std()
print("Desviación estándar de notas:", desv_notas)

# 4.4) Mínimo y máximo
min_notas = arr_notas.min()
max_notas = arr_notas.max()
print("Mínimo de notas:", min_notas)
print("Máximo de notas:", max_notas)

# -------------------------------------------------------------------
# 5) Redimensionar (reshape) un arreglo
# -------------------------------------------------------------------
# Supongamos que queremos tomar el arreglo 'arr_rango' (0 a 9)
# y reorganizarlo en una matriz de 2 filas y 5 columnas.

arr_rebanado = arr_rango.reshape((2, 5))
print("\n===== arr_rango original =====")
print(arr_rango)
print("\n===== arr_rango con reshape((2, 5)) =====")
print(arr_rebanado)
# Salida esperada:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]]

# -------------------------------------------------------------------
# 6) Indexación y rebanado (slicing)
# -------------------------------------------------------------------
# 6.1) Acceder a un elemento específico
#     Por ejemplo, en `arr_notas`, el primer elemento (índice 0) y el segundo (índice 1)
print("\n===== Indexación en arr_notas =====")
print("Primer elemento arr_notas[0]:", arr_notas[0])   # 75
print("Segundo elemento arr_notas[1]:", arr_notas[1])  # 82

# 6.2) Rebanar (slicing): obtener subarreglos
#     a) De arr_notas, tomar solo los primeros dos elementos
slice_notas = arr_notas[0:2]  # Desde índice 0 hasta índice 2 (sin incluir 2)
print("\nLos primeros dos elementos de arr_notas (arr_notas[0:2]):", slice_notas)
# Salida esperada: [75 82]

#     b) De arr_rebanado (matriz 2x5), tomar la fila 0 completa
fila0 = arr_rebanado[0, :]   # Filas se indican primero, luego columnas. ':' significa "todas las columnas"
print("\nFila 0 completa de arr_rebanado (arr_rebanado[0, :]):", fila0)
# Salida esperada: [0 1 2 3 4]

#     c) De arr_rebanado, tomar la columna 3 de ambas filas
col3 = arr_rebanado[:, 3]    # ':' en filas = todas las filas; 3 = columna índice 3
print("\nColumna 3 de arr_rebanado (arr_rebanado[:, 3]):", col3)
# Salida esperada: [3 8]

# -------------------------------------------------------------------
# 7) Operaciones avanzadas sencillas: broadcasting
# -------------------------------------------------------------------
# Supongamos que queremos restar el promedio de cada elemento de arr_notas
# Primero, calculamos el promedio
promedio = arr_notas.mean()
# Luego, restamos ese promedio a cada elemento. Gracias a "broadcasting", NumPy
# automáticamente aplica la resta a cada posición del arreglo.
arr_centrado = arr_notas - promedio

print("\n===== Operación de broadcasting =====")
print("arr_notas original:", arr_notas)
print("Promedio de arr_notas:", promedio)
print("arr_notas centrado (arr_notas - promedio):", arr_centrado)
# Ejemplo: si promedio = 80.0,
# arr_centrado = [75-80, 82-80, 78-80, 85-80] = [-5. 2. -2. 5.]

# -------------------------------------------------------------------
# FIN DEL SCRIPT
# -------------------------------------------------------------------
