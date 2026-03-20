import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys

# -----------------------------
# FUNCIÓN PARA SALIR
# -----------------------------
def salir():
    st.warning("Saliendo de la aplicación...")
    st.stop()  # Detiene la ejecución

# -----------------------------
# DATOS
# -----------------------------
data = {
    "Autor": [
        "García & Crespo", "Martínez", "Hariyanto", "Fu", "Garzón",
        "Cotilla", "Bond", "Yim & Su", "Acuña-Gamboa", "Aparicio",
        "Barros", "Lumbi", "Macías", "Peñalver", "Hoana"
    ],
    "Año": [
        2024, 2025, 2025, 2025, 2025,
        2025, 2024, 2025, 2025, 2025,
        2025, 2025, 2025, 2024, 2025
    ],
    "Tipo": [
        "Beneficio", "Mixto", "Beneficio", "Beneficio", "Mixto",
        "Reto", "Mixto", "Beneficio", "Reto", "Beneficio",
        "Beneficio", "Beneficio", "Beneficio", "Mixto", "Beneficio"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
st.set_page_config(page_title="Dashboard IA", layout="wide")

st.title("📊 Dashboard: IA en la Educación")

# -----------------------------
# TABS (SECCIONES)
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Artículos",
    "📈 Análisis por Año",
    "🧠 Beneficios vs Retos",
    "📌 Conclusiones"
])

# -----------------------------
# TAB 1: ARTÍCULOS
# -----------------------------
with tab1:
    st.subheader("📚 Tabla de artículos")

    st.dataframe(df)

    if st.button("Salir", key="salir1"):
        salir()

# -----------------------------
# TAB 2: ANÁLISIS POR AÑO
# -----------------------------
with tab2:
    st.subheader("📈 Artículos por año")

    articulos_por_año = df["Año"].value_counts().sort_index()

    fig1, ax1 = plt.subplots()
    ax1.bar(articulos_por_año.index, articulos_por_año.values)
    ax1.set_xlabel("Año")
    ax1.set_ylabel("Cantidad")
    ax1.set_title("Número de artículos por año")

    st.pyplot(fig1)

    if st.button("Salir", key="salir2"):
        salir()

# -----------------------------
# TAB 3: BENEFICIOS VS RETOS
# -----------------------------
with tab3:
    st.subheader("🧠 Distribución de enfoques")

    tipo_counts = df["Tipo"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(tipo_counts, labels=tipo_counts.index, autopct='%1.1f%%')
    ax2.set_title("Beneficios vs Retos")

    st.pyplot(fig2)

    if st.button("Salir", key="salir3"):
        salir()

# -----------------------------
# TAB 4: CONCLUSIONES
# -----------------------------
with tab4:
    st.subheader("📌 Conclusiones")

    st.write("""
    - La IA mejora el aprendizaje personalizado.
    - Incrementa la motivación estudiantil.
    - Existen retos como la ética, el acceso y la dependencia tecnológica.
    """)

    if st.button("Salir", key="salir4"):
        salir()
