import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="IA en la Educación", layout="wide")

# -----------------------------
# ESTADO PARA SALIR
# -----------------------------
if "salir" not in st.session_state:
    st.session_state["salir"] = False

def salir():
    st.session_state["salir"] = True

if st.session_state["salir"]:
    st.title("👋 Gracias por usar la app")
    st.stop()

# -----------------------------
# DATOS COMPLETOS DEL DOCUMENTO
# -----------------------------
data = [
    ["García & Crespo", 2024, "Mixto", "Uso de tecnologías digitales mejora aprendizaje pero depende del acceso"],
    ["Martínez", 2025, "Mixto", "IA generativa automatiza tareas y personaliza aprendizaje, pero puede afectar habilidades críticas"],
    ["Hariyanto", 2025, "Beneficio", "Machine learning permite aprendizaje personalizado en tiempo real"],
    ["Fu", 2025, "Beneficio", "IA impacta enseñanza, aprendizaje y administración educativa"],
    ["Garzón", 2025, "Mixto", "Mejora motivación y aprendizaje, pero presenta retos éticos y tecnológicos"],
    ["Cotilla", 2025, "Reto", "Problemas de inclusión, sesgos y desigualdad de acceso"],
    ["Bond", 2024, "Mixto", "Personalización, sistemas adaptativos y evaluación automatizada"],
    ["Yim & Su", 2025, "Beneficio", "Alfabetización en IA mejora habilidades digitales y pensamiento computacional"],
    ["Acuña-Gamboa", 2025, "Reto", "Sesgos, ética y uso crítico en investigación"],
    ["Aparicio", 2025, "Beneficio", "Mejora rendimiento, motivación y autonomía del estudiante"],
    ["Barros", 2025, "Beneficio", "Mejora aprendizaje en matemáticas y ciencias"],
    ["Lumbi", 2025, "Beneficio", "Retroalimentación inmediata y adaptación de contenidos"],
    ["Macías", 2025, "Beneficio", "Favorece inclusión y aprendizaje personalizado"],
    ["Peñalver", 2024, "Mixto", "Educación 4.0, automatización y aprendizaje adaptativo"],
    ["Hoana", 2025, "Beneficio", "Transforma la experiencia educativa"],
    ["Chen & Pérez", 2023, "Beneficio", "Adaptación de contenidos y evaluación del progreso"],
    ["Sadiku", 2021, "Beneficio", "Automatización y mejora de enseñanza"],
    ["Martínez-Márquez", 2025, "Mixto", "IA como tecnología disruptiva con retos educativos"]
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
Permite personalizar el aprendizaje, mejorar la motivación y facilitar nuevas formas de enseñanza.

Desde 2022, la IA generativa ha cambiado la forma en que estudiantes y docentes interactúan.
    """)

    st.subheader("Temas clave")
    st.markdown("""
- Aprendizaje adaptativo  
- Tutores inteligentes  
- Alfabetización en IA  
- Inclusión educativa  
- Ética y desafíos tecnológicos  
    """)

    if st.button("Salir", key="t1"):
        salir()

# -----------------------------
# TAB 2: ARTÍCULOS
# -----------------------------
with tab2:
    st.header("📚 Artículos analizados")

    st.dataframe(df, use_container_width=True)

    autor = st.selectbox("Selecciona un autor:", df["Autor"].tolist())

    resumen = df.loc[df["Autor"] == autor, "Resumen"].values
    if len(resumen) > 0:
        st.subheader("Resumen")
        st.write(resumen[0])

    if st.button("Salir", key="t2"):
        salir()

# -----------------------------
# TAB 3: ANÁLISIS
# -----------------------------
with tab3:
    st.header("📈 Análisis")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total artículos", len(df))
    col2.metric("Años analizados", df["Año"].nunique())
    col3.metric("Autores", df["Autor"].nunique())

    conteo_año = df["Año"].value_counts().sort_index()

    fig1, ax1 = plt.subplots()
    ax1.bar(conteo_año.index, conteo_año.values)
    ax1.set_xlabel("Año")
    ax1.set_ylabel("Cantidad")
    ax1.set_title("Artículos por año")
    plt.tight_layout()

    st.pyplot(fig1)

    if st.button("Salir", key="t3"):
        salir()

# -----------------------------
# TAB 4: BENEFICIOS Y RETOS
# -----------------------------
with tab4:
    st.header("🧠 Beneficios y Retos")

    conteo_tipo = df["Tipo"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(conteo_tipo, labels=conteo_tipo.index, autopct='%1.1f%%')
    ax2.set_title("Distribución")
    plt.tight_layout()

    st.pyplot(fig2)

    st.subheader("Beneficios")
    st.markdown("""
- Personalización del aprendizaje  
- Mejora del rendimiento académico  
- Mayor motivación  
- Inclusión educativa  
- Automatización de tareas  
    """)

    st.subheader("Retos")
    st.markdown("""
- Problemas éticos  
- Sesgos en los algoritmos  
- Dependencia tecnológica  
- Desigualdad de acceso  
- Falta de capacitación docente  
    """)

    if st.button("Salir", key="t4"):
        salir()

# -----------------------------
# TAB 5: CONCLUSIONES
# -----------------------------
with tab5:
    st.header("📌 Conclusiones")

    st.write("""
La inteligencia artificial representa una gran oportunidad para transformar la educación.

Permite adaptar el aprendizaje a cada estudiante, mejorar resultados y fomentar la inclusión.

Sin embargo, su implementación debe ser ética, responsable y accesible para todos.
    """)

    if st.button("Salir", key="t5"):
        salir()

