# demo_pandas.py

"""
Demo muy sencilla de pandas.
Este script muestra cómo:
  1) Importar pandas.
  2) Leer un archivo CSV (por ejemplo, datos_alumnos.csv).
  3) Ver las primeras filas con head().
  4) Obtener estadísticas descriptivas con describe().
  5) Calcular columnas nuevas (por ejemplo, promedio de notas).
  6) Ordenar el DataFrame según una columna.
  7) Filtrar filas según una condición.
  
Para ejecutarlo:
  1. Asegúrate de tener instalado pandas:
       pip install pandas
"""

import pandas as pd  # Importar la librería pandas con alias 'pd'

# 1) Leer el CSV en un DataFrame
# Suponemos que 'datos_alumnos.csv' existe en la misma carpeta
df = pd.read_csv("datos_alumnos.csv")

# 2) Mostrar las primeras filas del DataFrame
print("===== Primeras 5 filas del DataFrame =====")
print(df.head(5))  # head(5) muestra las primeras 5 filas

# 3) Mostrar estadísticas descriptivas de las columnas numéricas
print("\n===== Estadísticas descriptivas =====")
print(df.describe())  
# describe() muestra conteo, media, desviación estándar, mínimo, percentiles y máximo

# 4) Calcular una columna nueva: promedio de las 4 notas
# Crear una nueva columna llamada 'promedio'
df["promedio"] = (df["pep1"] + df["pep2"] + df["control1"] + df["control2"]) / 4

# Mostrar el DataFrame con la columna nueva
print("\n===== DataFrame con columna 'promedio' =====")
print(df[["nombre", "pep1", "pep2", "control1", "control2", "promedio"]])

# 5) Ordenar el DataFrame según el promedio, de mayor a menor
df_ordenado = df.sort_values(by="promedio", ascending=False)

print("\n===== DataFrame ordenado por promedio (descendente) =====")
print(df_ordenado[["nombre", "promedio"]])

# 6) Filtrar los alumnos que tengan promedio >= 85
filtro_alto = df[df["promedio"] >= 85]

print("\n===== Alumnos con promedio >= 85 =====")
print(filtro_alto[["nombre", "promedio"]])

# 7) Guardar el DataFrame ordenado en un nuevo CSV (opcional)
df_ordenado.to_csv("datos_alumnos_ordenado.csv", index=False)
print("\nSe ha guardado el DataFrame ordenado en 'datos_alumnos_ordenado.csv'")
