# demo_streamlit_explicativo.py

"""
Demo explicativa de Streamlit para estudiantes iniciados en Python.
Proposito: mostrar de forma muy comentada y paso a paso cómo:
  1) Cargar un CSV muy sencillo.
  2) Mostrar datos crudos en una tabla.
  3) Crear un gráfico de barras verticales.
  4) Crear un gráfico de líneas.
  5) Crear un gráfico de área.
  
En esta demo:
- NO usamos diccionarios, tuplas, ni comprensiones de listas.
- NO usamos f-strings; solo concatenación de cadenas.
- NO usamos "break" ni estructuras avanzadas.
- TODO se hace con listas, bucles y operaciones básicas.
"""

# --- Importar librerías necesarias ---
import streamlit as st      # Librería principal para crear la app
import csv                  # Para leer archivos CSV (sin pandas)

# --- Configuración general de la página ---
st.set_page_config(
    page_title="Demo Streamlit Iniciados",  # Título que aparece en la pestaña del navegador
    layout="wide"                           # Ocupa todo el ancho disponible
)

# --- Título principal de la aplicación ---
st.title("Demo Explicativa de Streamlit para Iniciados")
st.write("Esta app muestra ejemplos básicos de cómo usar Streamlit para cargar datos y dibujar gráficos simples.")

# --- Sidebar: Logo y enlaces ---
# Logo de Usach Premium
st.sidebar.image(
    "./images/logoDark.png",  # Muestra el logo en la barra lateral
    use_container_width=True  # Ajusta el tamaño del logo al contenedor
)

# Sección de Usach Premium con íconos sociales
st.sidebar.markdown("# Usach Premium", unsafe_allow_html=True)  # Muestra el título de la sección en la barra lateral
st.sidebar.markdown(
    """
    <div style="display: flex; gap: 10px;">
        <a href="https://www.youtube.com/@UsachPremium?sub_confirmation=1" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=85162&format=png&color=000000" alt="YouTube" width="24"/>
        </a>
        <a href="https://www.instagram.com/usach.premium/" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=32320&format=png&color=000000" alt="Instagram" width="24"/>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Barra lateral: navegación entre páginas ---
st.sidebar.title("Menú de navegación")
# Lista sencilla de nombres de las "pestañas"
opciones = ["Cargar datos", "Barras verticales", "Gráfico de líneas", "Gráfico de área","Try/Except"]
# Usamos radio para que el usuario escoja la sección que quiere ver
pagina = st.sidebar.radio("Selecciona una sección:", opciones)

st.sidebar.markdown("---")

# Sección del autor con LinkedIn y GitHub
st.sidebar.markdown("### Autor", unsafe_allow_html=True)
st.sidebar.markdown("**Byron Caices**")
st.sidebar.markdown(
    """
    <div style="display: flex; gap: 10px;">
        <a href="https://www.linkedin.com/in/byron-caices/" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="24"/>
        </a>
        <a href="https://github.com/ByronCaices/streamlit-demo" target="_blank">
            <img src="https://img.icons8.com/ios-glyphs/48/000000/github.png" alt="GitHub" width="24"/>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Función para cargar datos del CSV ---
@st.cache_data
def cargar_datos(path_csv):
    """
    Lee un archivo CSV muy simple y devuelve:
      - encabezados: lista de cadenas con los nombres de columnas
      - filas   : lista de filas, donde cada fila es a su vez una lista de cadenas
    Ejemplo de retorno:
      encabezados = ["nombre", "pep1", "pep2", "control1", "control2"]
      filas = [
        ["Ana Pérez", "75", "82", "78", "85"],
        ["Juan Soto", "88", "91", "84", "90"],
        ...
      ]
    """
    filas = []  # Lista vacía donde guardaremos cada fila leída del CSV
    with open(path_csv, "r", encoding="utf-8") as f:
        lector = csv.reader(f)       # Crea un objeto lector de CSV
        encabezados = next(lector)   # Lee la primera línea como encabezados
        # Recorre cada línea restante y la agrega a 'filas'
        for fila in lector:
            filas.append(fila)
    return encabezados, filas

# --- Intentamos cargar el CSV con los datos de los alumnos ---
ruta_archivo = "datos_alumnos.csv"  # Nombre del CSV que creamos arriba
enc, datos = [], []

# Capturamos errores si el archivo no existe o algo falla
try:
    encabezados, datos = cargar_datos(ruta_archivo)
except Exception as e:
    st.error("Error al leer el CSV: " + str(e))

# ------------------------------------------------------------------------
# 1) PÁGINA: "Cargar datos"
# ------------------------------------------------------------------------
if pagina == "Cargar datos":
    st.header("1. Cargar datos desde CSV")
    st.write("En esta sección mostramos cómo leer un CSV muy sencillo y ver los datos crudos.")

    st.write("**Pasos para leer un CSV con `csv.reader` y mostrar los encabezados y las primeras filas:**")
    # Ejemplo de fragmento de código para que los estudiantes vean cómo funciona:
    codigo_ejemplo = '''
# Primero: Importar la librería csv
import csv

# Abrir el archivo en modo lectura
with open("datos_alumnos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)           # Creamos un lector de CSV
    encabezados = next(lector)       # La primera línea son los encabezados
    filas = []
    for fila in lector:
        filas.append(fila)           # Cada 'fila' es una lista de cadenas

# Ahora tenemos:
#   encabezados = ["nombre", "pep1", "pep2", "control1", "control2"]
#   filas = [
#     ["Ana Pérez", "75", "82", "78", "85"],
#     ["Juan Soto", "88", "91", "84", "90"],
#     ...
#   ]
'''
    # Mostrar el fragmento de código en un recuadro
    st.code(codigo_ejemplo, language="python")

    # Ahora, en la app misma, mostramos lo que cargamos:
    if encabezados and datos:
        st.subheader("Encabezados leídos:")
        # Concatenamos todos los encabezados en una única cadena
        linea_encabezados = ""
        for col in encabezados:
            # Si es la primera columna no agregamos coma al inicio
            if linea_encabezados == "":
                linea_encabezados = col
            else:
                linea_encabezados = linea_encabezados + ", " + col
        st.write(linea_encabezados)

        st.subheader("Primeras 5 filas de datos (datos crudos):")
        # Mostrar solo las primeras 5 filas para no saturar la pantalla
        for i in range(len(datos)):
            if i < 5:
                fila = datos[i]
                # Convertimos la lista de esa fila en una sola cadena para imprimir
                texto_fila = ""
                for j in range(len(fila)):
                    if texto_fila == "":
                        texto_fila = fila[j]
                    else:
                        texto_fila = texto_fila + ", " + fila[j]
                st.write(str(i + 1) + ". " + texto_fila)
            else:
                break
    else:
        st.write("No se pudo leer el archivo CSV o está vacío.")

# ------------------------------------------------------------------------
# 2) PÁGINA: "Barras verticales"
# ------------------------------------------------------------------------
elif pagina == "Barras verticales":
    st.header("2. Gráfico de barras verticales")
    st.write(
        "En esta sección veremos cómo usar `st.bar_chart` para dibujar un gráfico "
        "de barras verticales con Streamlit."
    )
    st.write("**¿Qué vamos a graficar?**")
    st.write(
        "- Por cada alumno calcularemos su **promedio general** (sumando 4 notas y dividiendo por 4).  \n"
        "- Luego, mostraremos cómo usar `st.bar_chart(lista_de_promedios)` para ver la comparación."
    )

    # --- Explicar el fragmento de código que hace el cálculo de promedios ---
    codigo_calcular_promedios = '''
# Supongamos que 'datos' es una lista de filas, donde cada fila es:
#   ["Ana Pérez", "75", "82", "78", "85"], etc.

# 1) Crear lista vacía para promedios:
promedios = []

# 2) Recorrer cada fila de datos:
for fila in datos:
    # Convertir cada nota (cadena) a entero
    nota1 = int(fila[1])   # pep1
    nota2 = int(fila[2])   # pep2
    nota3 = int(fila[3])   # control1
    nota4 = int(fila[4])   # control2

    # Sumar las 4 notas:
    suma_notas = nota1 + nota2 + nota3 + nota4

    # Calcular promedio (dividimos entre 4)
    promedio = suma_notas / 4

    # Agregar el promedio a la lista
    promedios.append(promedio)

# Ahora 'promedios' es, por ejemplo: [80.0, 88.25, 68.75, 92.25, 79.5]
# donde el primer elemento corresponde a "Ana Pérez", el segundo a "Juan Soto", etc.
'''
    st.subheader("Fragmento de código para calcular promedios")
    st.code(codigo_calcular_promedios, language="python")

    # --- Ahora ejecutamos el cálculo dentro de la app ---
    promedios = []  # Inicializamos lista vacía
    # Recorremos cada fila en 'datos'
    for fila in datos:
        try:
            nota1 = int(fila[1])
            nota2 = int(fila[2])
            nota3 = int(fila[3])
            nota4 = int(fila[4])
            suma_notas = nota1 + nota2 + nota3 + nota4
            promedio_ind = suma_notas / 4
        except:
            # Si alguna conversión falla, ponemos promedio 0
            promedio_ind = 0
        promedios.append(promedio_ind)

    # Mostrar los promedios junto a los nombres para mayor claridad
    st.subheader("Promedios calculados por alumno:")
    for idx in range(len(datos)):
        nombre = datos[idx][0]              # Columna 0 = nombre del alumno
        prom = promedios[idx]               # Promedio calculado correspondiente
        # Concatenamos en una cadena para mostrar: "Ana Pérez: 80.0"
        linea = nombre + ": " + str(round(prom, 2))
        st.write(linea)

    # --- Finalmente: mostrar el gráfico de barras ---
    st.subheader("Gráfico de barras verticales con `st.bar_chart`")
    st.write(
        "Usamos `st.bar_chart(promedios)` para dibujar las barras.  \n"
        "- Cada barra está indexada por posición (0, 1, 2, …).  \n"
        "- El valor de la altura de la barra es el promedio."
    )
    # Mostrar un fragmento de código
    codigo_chart = '''
# Para dibujar un gráfico de barras verticales con Streamlit:
# Simplemente pasamos la lista 'promedios' a st.bar_chart:
st.bar_chart(promedios)
'''
    st.code(codigo_chart, language="python")

    # Renderizar el gráfico de barras
    st.bar_chart(promedios)

# ------------------------------------------------------------------------
# 3) PÁGINA: "Gráfico de líneas"
# ------------------------------------------------------------------------
elif pagina == "Gráfico de líneas":
    st.header("3. Gráfico de líneas")
    st.write(
        "Aquí veremos cómo usar `st.line_chart` para dibujar un gráfico de líneas.  \n"
        "Usaremos la misma lista de promedios calculada en la sección anterior."
    )

    # Explicación previa: construir la lista de promedios (volver a calcular)
    st.subheader("Recalculamos la lista de promedios (si no venimos de la pestaña anterior):")
    codigo_recalcular = '''
# Volvemos a calcular la lista 'promedios' en caso de no tenerla ya
promedios = []
for fila in datos:
    try:
        nota1 = int(fila[1]); nota2 = int(fila[2])
        nota3 = int(fila[3]); nota4 = int(fila[4])
        promedio_ind = (nota1 + nota2 + nota3 + nota4) / 4
    except:
        promedio_ind = 0
    promedios.append(promedio_ind)
'''
    st.code(codigo_recalcular, language="python")

    # Ejecutamos el cálculo nuevamente
    promedios = []
    for fila in datos:
        try:
            nota1 = int(fila[1]); nota2 = int(fila[2])
            nota3 = int(fila[3]); nota4 = int(fila[4])
            prom = (nota1 + nota2 + nota3 + nota4) / 4
        except:
            prom = 0
        promedios.append(prom)

    st.write("Promedios disponibles:", promedios)

    # Mostrar fragmento de código para la línea
    st.subheader("Fragmento de código para `st.line_chart`")
    codigo_line = '''
# Para dibujar un gráfico de líneas con Streamlit:
# Solo pasamos la lista 'promedios' a st.line_chart:
st.line_chart(promedios)
'''
    st.code(codigo_line, language="python")

    # Renderizar el gráfico de líneas
    st.line_chart(promedios)

# ------------------------------------------------------------------------
# 4) PÁGINA: "Gráfico de área"
# ------------------------------------------------------------------------
elif pagina == "Gráfico de área":
    st.header("4. Gráfico de área")
    st.write(
        "En esta sección mostraremos cómo usar `st.area_chart` para dibujar un gráfico de área.  \n"
        "Este tipo de gráfico es similar al de líneas, pero rellena el área debajo de la curva."
    )

    # Volver a calcular promedios para este ejemplo
    st.subheader("Volvemos a calcular la lista de promedios:")
    codigo_recalcular2 = '''
promedios = []
for fila in datos:
    try:
        nota1 = int(fila[1]); nota2 = int(fila[2])
        nota3 = int(fila[3]); nota4 = int(fila[4])
        prom = (nota1 + nota2 + nota3 + nota4) / 4
    except:
        prom = 0
    promedios.append(prom)
'''
    st.code(codigo_recalcular2, language="python")

    promedios = []
    for fila in datos:
        try:
            nota1 = int(fila[1]); nota2 = int(fila[2])
            nota3 = int(fila[3]); nota4 = int(fila[4])
            prom = (nota1 + nota2 + nota3 + nota4) / 4
        except:
            prom = 0
        promedios.append(prom)

    st.write("Promedios calculados:", promedios)

    # Mostrar fragmento de código para área
    st.subheader("Fragmento de código para `st.area_chart`")
    codigo_area = '''
# Para dibujar un gráfico de área:
st.area_chart(promedios)
'''
    st.code(codigo_area, language="python")

    # Renderizar el gráfico de área
    st.area_chart(promedios)

# ------------------------------------------------------------------------
# 5) PÁGINA: "Try/Except"
# ------------------------------------------------------------------------
elif pagina == "Try/Except":
    st.header("5. ¿Qué es try/except y por qué lo usamos?")
    st.write(
        "Cuando leemos datos de un CSV (u otras operaciones que pueden fallar), "
        "es posible que ocurra un error (por ejemplo, que no exista el archivo, "
        "o que una cadena no se pueda convertir a número).  \n\n"
        "**`try/except`** es la forma en Python de “probar” un bloque de código y, "
        "si ocurre un error, ejecutar otro bloque que lo maneje en lugar de detener "
        "todo el programa."
    )

    st.subheader("Ejemplo básico de try/except:")
    st.write(
        "Supongamos que queremos convertir una cadena a entero.  \n"
        "- Si la cadena es \"75\", todo va bien y obtenemos el entero 75.  \n"
        "- Si la cadena es \"abc\", Python lanzará un error `ValueError`.  \n\n"
        "Con `try/except` podemos capturar ese error y asignar un valor por defecto."
    )

    # Fragmento de código muy comentado que explica cada línea
    ejemplo_try_except = '''
# Imaginemos una lista de cadenas que representan notas:
lista_cadenas = ["75", "82", "abc", "90"]

# Lista vacía donde guardaremos los enteros válidos o 0 si falla la conversión
notas_convertidas = []

# Recorremos cada elemento de la lista de cadenas
for cad in lista_cadenas:
    try:
        # Intentamos convertir la cadena a entero
        num = int(cad)
    except:
        # Si falla (por ejemplo cad = "abc"), asignamos num = 0 en lugar de romper el programa
        num = 0
    # Agregamos el resultado (entero válido o 0) a nuestra lista
    notas_convertidas.append(num)

# Al final, notas_convertidas será [75, 82, 0, 90]
'''
    st.code(ejemplo_try_except, language="python")

    st.write(
        "- En este bloque:  \n"
        "  1. El `try:` intenta hacer `int(cad)`.  \n"
        "  2. Si `cad` no se puede convertir (por ejemplo, \"abc\"), Python salta al bloque `except:`.  \n"
        "  3. Dentro de `except:` le asignamos `num = 0` para que no falle el programa.  \n"
        "  4. Siempre agregamos `num` (sea la conversión real o el 0 por defecto) a `notas_convertidas`."
    )

    st.subheader("¿Por qué lo usamos en esta demo?")
    st.write(
        "- Al leer el CSV, algunas celdas pueden estar vacías o contener texto que no sea número.  \n"
        "- Si hacemos `int(fila[i])` sin protección y la celda no es un número válido, el programa se detendrá con un `ValueError`.  \n"
        "- Entonces envolvemos esa conversión en `try/except` para:  \n"
        "    1. Capturar el error.  \n"
        "    2. Asignar un valor seguro (por ejemplo, 0) cuando falle.  \n"
        "    3. Continuar ejecutando el dashboard sin que se rompa.  \n\n"
        "De esta forma garantizamos que todos los promedios o gráficos se calculen incluso si hay datos sucios o celdas vacías."
    )


# ------------------------------------------------------------------------
# FIN DEL SCRIPT
# ------------------------------------------------------------------------

