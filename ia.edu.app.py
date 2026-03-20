import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
st.set_page_config(page_title="IA en la Educación", layout="wide")

# -----------------------------
# CONTROL DE SALIDA
# -----------------------------
if "salir" not in st.session_state:
    st.session_state.salir = False

def salir():
    st.session_state.salir = True

if st.session_state.salir:
    st.title("👋 Gracias por usar el dashboard")
    st.stop()

# -----------------------------
# DATOS (basados en tu documento)
# -----------------------------
data = [
    ["García & Crespo", 2024, "Beneficio", "Tecnologías digitales mejoran aprendizaje pero requieren acceso"],
    ["Martínez", 2025, "Mixto", "IA generativa mejora aprendizaje pero puede afectar habilidades críticas"],
    ["Hariyanto", 2025, "Beneficio", "Aprendizaje personalizado con machine learning"],
    ["Fu", 2025, "Beneficio", "IA impacta enseñanza, aprendizaje y administración"],
    ["Garzón", 2025, "Mixto", "Mejora aprendizaje pero presenta retos éticos"],
    ["Cotilla", 2025, "Reto", "Problemas de equidad y sesgos"],
    ["Bond", 2024, "Mixto", "Personalización y evaluación automatizada"],
    ["Yim & Su", 2025, "Beneficio", "Alfabetización en IA mejora habilidades"],
    ["Acuña-Gamboa", 2025, "Reto", "Sesgos y problemas éticos"],
    ["Aparicio", 2025, "Beneficio", "Mejora rendimiento y motivación"],
    ["Barros", 2025, "Beneficio", "Mejora rendimiento en matemáticas y ciencias"],
    ["Lumbi", 2025, "Beneficio", "Retroalimentación inmediata"],
    ["Macías", 2025, "Beneficio", "Aprendizaje inclusivo"],
    ["Peñalver", 2024, "Mixto", "Educación 4.0 y automatización"],
    ["Hoana", 2025, "Beneficio", "Transforma la experiencia educativa"]
]

df = pd.DataFrame(data, columns=["Autor", "Año", "Tipo", "Resumen"])

# -----------------------------
# TÍTULO
# -----------------------------
st.title("📊 Dashboard: Inteligencia Artificial en la Educación")

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Introducción",
    "📚 Artículos",
    "📈 Análisis",
    "🧠 Beneficios y Retos",
    "📌 Conclusiones"
])

# -----------------------------
# TAB 1: INTRODUCCIÓN
# -----------------------------
with tab1:
    st.header("📖 Introducción")

    st.write("""
    La Inteligencia Artificial (IA) está transformando la educación en el siglo XXI.
    Permite personalizar el aprendizaje, mejorar la motivación estudiantil y optimizar
    los procesos educativos.

    Desde 2022, la IA generativa ha cambiado la relación entre estudiantes y docentes,
    facilitando nuevas formas de enseñanza y aprendizaje.
    """)

    st.subheader("🎯 Temas principales del documento:")
    st.markdown("""
    - Aprendizaje adaptativo  
    - Tutores inteligentes  
    - Alfabetización en IA  
    - Inclusión educativa  
    - Retos éticos y tecnológicos  
    """)

    if st.button("Salir", key="salir1"):
        salir()

# -----------------------------
# TAB 2: ARTÍCULOS
# -----------------------------
with tab2:
    st.header("📚 Artículos analizados")

    st.dataframe(df)

    autor = st.selectbox("Selecciona un autor:", df["Autor"])

    st.write("### Resumen:")
    st.write(df[df["Autor"] == autor]["Resumen"].values[0])

    if st.button("Salir", key="salir2"):
        salir()

# -----------------------------
# TAB 3: ANÁLISIS
# -----------------------------
with tab3:
    st.header("📈 Análisis de datos")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total artículos", len(df))
    col2.metric("Años analizados", df["Año"].nunique())
    col3.metric("Autores únicos", df["Autor"].nunique())

    st.subheader("Artículos por año")

    conteo_año = df["Año"].value_counts().sort_index()

    fig1, ax1 = plt.subplots()
    ax1.bar(conteo_año.index, conteo_año.values)
    ax1.set_xlabel("Año")
    ax1.set_ylabel("Cantidad")
    st.pyplot(fig1)

    if st.button("Salir", key="salir3"):
        salir()

# -----------------------------
# TAB 4: BENEFICIOS Y RETOS
# -----------------------------
with tab4:
    st.header("🧠 Beneficios vs Retos")

    conteo_tipo = df["Tipo"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(conteo_tipo, labels=conteo_tipo.index, autopct='%1.1f%%')
    st.pyplot(fig2)

    st.subheader("📌 Beneficios identificados:")
    st.markdown("""
    - Personalización del aprendizaje  
    - Mayor motivación estudiantil  
    - Inclusión educativa  
    - Automatización de tareas  
    """)

    st.subheader("⚠️ Retos identificados:")
    st.markdown("""
    - Problemas éticos  
    - Sesgos en los datos  
    - Dependencia tecnológica  
    - Falta de acceso  
    """)

    if st.button("Salir", key="salir4"):
        salir()

# -----------------------------
# TAB 5: CONCLUSIONES
# -----------------------------
with tab5:
    st.header("📌 Conclusiones")

    st.write("""
    La inteligencia artificial representa una oportunidad clave para mejorar la educación.
    Sin embargo, su implementación debe ser ética, inclusiva y equilibrada.

    No reemplaza a los docentes, sino que potencia el aprendizaje humano.
    """)

    if st.button("Salir", key="salir5"):
        salir()
