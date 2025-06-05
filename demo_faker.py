# generar_csv_alumnos.py

"""
Este script genera un archivo CSV llamado `datos_alumnos.csv` con la siguiente estructura:
    nombre,pep1,pep2,control1,control2

Utiliza la librería Faker para crear nombres aleatorios (en español) y el módulo random
para generar puntajes numéricos entre 60 y 100. La generación es reproducible gracias
a una semilla (seed) fija tanto para Faker como para random.

Para ejecutarlo, instale Faker si no lo tiene:
    pip install Faker
"""

import pandas as pd  # Importar pandas para manejar el CSV
import random
from faker import Faker

# -------------------------------
# 1. Configurar la semilla fija
# -------------------------------
SEED = 12345
random.seed(SEED)            # Semilla para random.randint
Faker.seed(SEED)             # Semilla para Faker
faker = Faker("es_CL")       # Faker configurado para nombres en español de Chile (opcional)

# -------------------------------
# 2. Definir el nombre del CSV
# -------------------------------
NOMBRE_ARCHIVO = "datos_alumnos_faker.csv"

# -------------------------------
# 3. Cantidad de filas a generar
# -------------------------------
NUM_ALUMNOS = 500  # Puedes cambiar este número si quieres más o menos filas

# -------------------------------
# 4. Rango de puntajes
# -------------------------------
MIN_NOTA = 40
MAX_NOTA = 70

# -------------------------------
# 5. Generar los datos
# -------------------------------
# Crear una lista de listas para almacenar los datos
datos = []
encabezados = ["nombre", "pep1", "pep2", "control1", "control2"]

for i in range(NUM_ALUMNOS):
    # Generar un nombre completo aleatorio
    nombre_alumno = faker.name()

    # Generar puntajes aleatorios para pep1, pep2, control1 y control2
    pep1 = random.randint(MIN_NOTA, MAX_NOTA)
    pep2 = random.randint(MIN_NOTA, MAX_NOTA)
    control1 = random.randint(MIN_NOTA, MAX_NOTA)
    control2 = random.randint(MIN_NOTA, MAX_NOTA)

    # Agregar los datos como una lista
    datos.append([nombre_alumno, pep1, pep2, control1, control2])

# Convertir la lista de listas en un DataFrame de pandas
df = pd.DataFrame(datos, columns=encabezados)

# Guardar el DataFrame como un archivo CSV
df.to_csv(NOMBRE_ARCHIVO, index=False, encoding="utf-8")

print("Se ha generado el archivo '" + NOMBRE_ARCHIVO + "' con " + str(NUM_ALUMNOS) + " filas de ejemplo.")
