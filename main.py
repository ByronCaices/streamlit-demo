# demo_streamlit.py

"""
Demo de Streamlit para Usach Premium Stats.
Muestra ejemplos de:
- Lectura de un CSV con csv.reader
- Visualización de datos crudos
- KPIs con st.metric y listado de top videos
- Gráficos de series de tiempo con Vega-Lite
- Histogramas, donut chart y barras para ayudantía
- Cálculo manual de estadísticas básicas
"""

import streamlit as st
import csv

# --- Configuración de la página ---
st.set_page_config(
    page_title="Dashboard: Usach Premium Stats",  # Configura el título de la página del navegador
    page_icon=":bar_chart:",  # Configura el ícono que aparece en la pestaña del navegador
    layout="wide"  # Configura el diseño de la página como ancho completo
)

# --- Definición de la paleta de colores ---
COLORS = {
    "primary": "#00A499",  # Color principal para elementos destacados
    "secondary": "#EA7600",  # Color secundario para elementos complementarios
    "tertiary": "#394049"  # Color terciario para fondos y texto
}

# --- Título y descripción general ---
st.title("Demo de Dashboard con Streamlit")  # Muestra el título principal del dashboard
st.markdown("Esta demo muestra cómo crear un dashboard interactivo con Streamlit, usando un CSV de ejemplo.")  # Muestra una descripción general del dashboard

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

# --- Sidebar: Navegación entre páginas ---
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", [
    "Datos crudos", "Visión general", "Series de tiempo", "Distribuciones", "Estadísticas"
])


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
@st.cache_data  # Cachea los datos para mejorar el rendimiento
def cargar_datos(path): # 
    """
    Carga el CSV y devuelve encabezados y lista de filas.
    Cada fila es una lista de strings.
    """
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)  # encabezados
        for row in reader:
            data.append(row)
    return headers, data

# --- Leer datos ---
data_path = "./Usach Premium STATS - YT-STATS.csv"
headers, data = cargar_datos(data_path)

# --- Página: Datos crudos ---
if page == "Datos crudos":
    st.header("Datos crudos")
    st.markdown("Se muestran los encabezados y los primeros registros tal cual se cargan.")
    st.write("Encabezados:", headers)
    st.write("Primeros registros:")
    st.dataframe(data[:10], use_container_width=True)

# --- Página: Visión general ---
elif page == "Visión general":
    st.header("Visión general")
    st.markdown("KPIs básicos y top 5 videos por vistas.")
    
    # 1) Total de videos
    total_videos = len(data)
    
    # 2) Total de vistas
    total_vistas = 0
    for row in data:
        total_vistas += int(row[7])
        
    # 3) Promedio de likes
    suma_likes = 0
    for row in data:
        suma_likes += int(row[8])
    # Calcular promedio de likes
    if total_videos == 0:
        promedio_likes = 0
    else:
        promedio_likes = round(suma_likes / total_videos, 2)

    # Mostrar las 3 métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de videos", total_videos)
    col2.metric("Total de vistas", total_vistas)
    col3.metric("Promedio de likes", promedio_likes)

    # --- Top 5 videos por vistas ---
    st.subheader("Top 5 videos por vistas")
    def get_vistas(row):
        try:
            return int(row[7])
        except:
            return 0
    top5 = sorted(data, key=get_vistas, reverse=True)[:5]
    for i, row in enumerate(top5, 1):
        st.write(str(i) + ". **" + row[1] + "**: " + str(get_vistas(row)) + " vistas")

# --- Página: Series de tiempo ---
elif page == "Series de tiempo":
    st.header("Series de tiempo")
    st.markdown("Gráfico de línea de métricas por video (orden cronológico).")
    
    # Definir opciones de métrica
    metric_options = {"Vistas": 7, "Likes": 8, "Comentarios": 9}
    metric_name = st.selectbox("Selecciona la métrica", list(metric_options.keys()))
    idx = metric_options[metric_name] # Índice de la métrica seleccionada
    
    # Construir lista de valores
    values = []
    for row in data:
        try:
            values.append(int(row[idx]))
        except:
            values.append(0)
    
    # Slider para número de puntos a graficar
    count = st.slider("Cantidad de videos a graficar", 1, len(values), len(values))
    
    # Preparar datos para Vega-Lite
    plot_data = []
    for i, v in enumerate(values[:count]):
        plot_data.append({"index": i + 1, metric_name: v})
    
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
    st.markdown("Histogramas y gráficos adicionales para explorar el dataset.")

    # -- Histograma de vistas --
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

    # -- Gráfico de anillo: vistas promedio por playlist --
    st.subheader("Vistas promedio por Playlist")
    # Obtener playlists únicas
    playlists = []
    for row in data:
        pl = row[4]
        if pl not in playlists:
            playlists.append(pl)
    # Calcular promedio de vistas por playlist
    playlist_avg = []
    for pl in playlists:
        total = 0
        count_pl = 0
        for row in data:
            if row[4] == pl:
                try:
                    total += int(row[7])
                    count_pl += 1
                except:
                    pass
        avg = total / count_pl if count_pl else 0
        playlist_avg.append({"playlist": pl, "avg_vistas": round(avg, 2)})
    # Vega-Lite donut
    donut_spec = {
        "mark": {"type": "arc", "innerRadius": 50},
        "encoding": {
            "theta": {"field": "avg_vistas", "type": "quantitative", "title": "Vistas promedio"},
            "color": {"field": "playlist", "type": "nominal", "scale": {"scheme": "category10"}}
        }
    }
    st.vega_lite_chart(playlist_avg, donut_spec, use_container_width=True)

    # -- Horas de ayudantía por ayudante --
    st.subheader("Horas de ayudantía por Ayudante")
    # Función para convertir 'H:MM:SS' a horas decimales
    def parse_horas(s):
        parts = s.split(":")
        try:
            if len(parts) == 3:
                h, m, sec = map(int, parts)
            elif len(parts) == 2:
                h = 0
                m, sec = map(int, parts)
            else:
                return 0
            return h + m / 60 + sec / 3600
        except:
            return 0

    # Agrupar y sumar horas por ayudante
    ayudantes = []
    for row in data:
        ay = row[14]
        if ay and ay not in ayudantes:
            ayudantes.append(ay)
    horas_by_ayu = []
    for ay in ayudantes:
        total_h = 0
        for row in data:
            if row[14] == ay:
                total_h += parse_horas(row[3])
        horas_by_ayu.append({"ayudante": ay, "horas": round(total_h, 2)})

    # Barra vertical con Vega-Lite
    bar_spec = {
        "mark": {"type": "bar", "color": COLORS["primary"]},
        "encoding": {
            "x": {"field": "ayudante", "type": "nominal", "title": "Ayudante", "axis": {"labelAngle": -45}},
            "y": {"field": "horas", "type": "quantitative", "title": "Horas"}
        }
    }
    st.vega_lite_chart(horas_by_ayu, bar_spec, use_container_width=True)

# --- Página: Estadísticas ---
elif page == "Estadísticas":
    st.header("Estadísticas")
    st.markdown("Cálculo manual de media, mediana, desviación estándar, mínimo y máximo.")

    # Extraer lista de vistas
    vistas = []
    for row in data:
        try:
            vistas.append(int(row[7]))
        except:
            pass

    # Función para media
    def calcular_media(valores):
        total = 0
        for x in valores:
            total += x
        return total / len(valores) if valores else 0

    # Función para mediana
    def calcular_mediana(valores):
        sorted_vals = sorted(valores)
        n = len(sorted_vals)
        if n == 0:
            return 0
        if n % 2 == 1:
            return sorted_vals[n // 2]
        else:
            return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2

    # Función para desviación estándar
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
