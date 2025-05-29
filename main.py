# demo_streamlit.py
"""
Demo de Streamlit para Usach Premium Stats.
Muestra ejemplos de:
- Lectura de un CSV con csv.reader
- Visualización de datos crudos
- KPIs con st.metric
- Gráficos de series de tiempo con Vega-Lite
- Histogramas y boxplots con Vega-Lite
- Cálculo manual de estadísticas básicas
"""

import streamlit as st
import csv

# Configuración de la página: fondo blanco por defecto y diseño ancho
st.set_page_config(
    page_title="Dashboard: Usach Premium Stats",
    page_icon=":bar_chart:",
    layout="wide"
)

# Definición de la paleta de colores usada en los gráficos
COLORS = {
    "primary": "#00A499",
    "secondary": "#EA7600",
    "tertiary": "#394049"
}

# Título principal en la página
st.title("Demo de Dashboard con Streamlit")
st.markdown("Este demo muestra cómo crear un dashboard interactivo con Streamlit, usando un CSV de ejemplo.")

# Sidebar para navegar entre distintas vistas de la app
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", [
    "Datos crudos", "Visión general", "Series de tiempo", "Distribuciones", "Estadísticas"
])

# Función para cargar datos desde CSV y devolver encabezados y registros
@st.cache_data
def cargar_datos(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)  # primera línea con nombres de columnas
        for row in reader:
            data.append(row)  # cada row es una lista de strings
    return headers, data

# Ruta del archivo CSV subido
data_path = "./Usach Premium STATS - YT-STATS.csv"
headers, data = cargar_datos(data_path)

# --- Página: Datos crudos ---
if page == "Datos crudos":
    st.header("Datos crudos")
    st.markdown("A continuación se muestran los encabezados y los primeros registros cargados manualmente.")
    # Mostrar lista de encabezados
    st.write("Encabezados:", headers)
    # Mostrar las primeras 10 filas de datos
    st.write("Primeros registros:")
    st.write(data[:10])

# --- Página: Visión general ---
elif page == "Visión general":
    st.header("Visión general")
    st.markdown("KPIs básicos calculados a partir del dataset.")
    # Total de videos (filas del CSV)
    total_videos = len(data)
    # Suma de todas las vistas (columna índice 7)
    total_vistas = 0
    for row in data:
        try:
            total_vistas += int(row[7])
        except:
            pass
    # Promedio de likes (columna índice 8)
    suma_likes = 0
    for row in data:
        try:
            suma_likes += int(row[8])
        except:
            pass
    promedio_likes = round(suma_likes / total_videos, 2) if total_videos > 0 else 0

    # Mostrar métricas en tres columnas
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de videos", total_videos)
    col2.metric("Total de vistas", total_vistas)
    col3.metric("Promedio de likes", promedio_likes)

# --- Página: Series de tiempo ---
elif page == "Series de tiempo":
    st.header("Series de tiempo")
    st.markdown("Gráfico de línea de métricas por video (orden cronológico). Siembra un índice para simplificar.")
    # Opciones de métrica y su columna correspondiente
    metric_options = {"Vistas": 7, "Likes": 8, "Comentarios": 9}
    metric_name = st.selectbox("Selecciona la métrica", list(metric_options.keys()))
    idx = metric_options[metric_name]
    # Construir lista de valores numéricos
    values = []
    for row in data:
        try:
            values.append(int(row[idx]))
        except:
            values.append(0)
    # Slider para definir cuántos puntos graficar
    count = st.slider("Cantidad de videos a graficar", 1, len(values), len(values))
    # Preparar datos para Vega-Lite
    plot_data = []
    for i, v in enumerate(values[:count]):
        plot_data.append({"index": i+1, metric_name: v})
    # Spec de Vega-Lite con color primario
    spec = {
        "mark": {"type": "line", "color": COLORS["primary"]},
        "encoding": {
            "x": {"field": "index", "type": "quantitative", "title": "Video (orden)"},
            "y": {"field": metric_name, "type": "quantitative", "title": metric_name}
        }
    }
    st.vega_lite_chart(plot_data, spec, use_container_width=True)

# --- Página: Distribuciones ---
elif page == "Distribuciones":
    st.header("Distribuciones")
    st.markdown("Histogramas y boxplot de métricas para explorar distribuciones.")
    # Histograma de vistas
    hist_data = []
    for row in data:
        try:
            hist_data.append({"vistas": int(row[7])})
        except:
            pass
    hist_spec = {
        "mark": {"type": "bar", "color": COLORS["secondary"]},
        "encoding": {
            "x": {"field": "vistas", "type": "quantitative", "bin": {"maxbins": 20}, "title": "Vistas"},
            "y": {"aggregate": "count", "type": "quantitative", "title": "Frecuencia"}
        }
    }
    st.subheader("Histograma de vistas")
    st.vega_lite_chart(hist_data, hist_spec, use_container_width=True)
    # Boxplot de likes
    box_data = []
    for row in data:
        try:
            box_data.append({"likes": int(row[8])})
        except:
            pass
    box_spec = {
        "mark": {"type": "boxplot", "color": COLORS["tertiary"]},
        "encoding": {"y": {"field": "likes", "type": "quantitative", "title": "Likes"}}
    }
    st.subheader("Boxplot de likes")
    st.vega_lite_chart(box_data, box_spec, use_container_width=True)

# --- Página: Estadísticas ---
elif page == "Estadísticas":
    st.header("Estadísticas")
    st.markdown("Cálculo manual de media, mediana, desviación estándar, mínimo y máximo.")
    # Extraer lista de vistas para los cálculos
    vistas = []
    for row in data:
        try:
            vistas.append(int(row[7]))
        except:
            pass
    # Definir funciones manuales
    def calcular_media(valores):
        total = 0
        for x in valores:
            total += x
        return total / len(valores) if valores else 0

    def calcular_mediana(valores):
        sorted_vals = sorted(valores)
        n = len(sorted_vals)
        if n == 0:
            return 0
        if n % 2 == 1:
            return sorted_vals[n//2]
        else:
            return (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2

    def calcular_desviacion_estandar(valores):
        media = calcular_media(valores)
        suma_diff = 0
        for x in valores:
            suma_diff += (x - media) ** 2
        varianza = suma_diff / len(valores) if valores else 0
        return varianza ** 0.5

    # Realizar cálculos
    media_v = calcular_media(vistas)
    mediana_v = calcular_mediana(vistas)
    desv_v = calcular_desviacion_estandar(vistas)
    min_v = min(vistas) if vistas else 0
    max_v = max(vistas) if vistas else 0

    # Mostrar resultados
    st.write(f"**Media de vistas:** {media_v:.2f}")
    st.write(f"**Mediana de vistas:** {mediana_v:.2f}")
    st.write(f"**Desviación estándar de vistas:** {desv_v:.2f}")
    st.write(f"**Mínimo de vistas:** {min_v}")
    st.write(f"**Máximo de vistas:** {max_v}")
