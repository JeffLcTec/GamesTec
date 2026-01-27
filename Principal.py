import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os

# ----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ----------------------------
st.set_page_config(page_title="GamesTEC", layout="wide")

# ----------------------------
# CARGA DE DATOS (SIN FIREBASE)
# ----------------------------
with open("JuegosActualizado.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with open("imagenes.json", "r", encoding="utf-8") as file:
    imagenes = json.load(file)

if 'juego_seleccionado' in st.session_state:
    st.session_state.pop('juego_seleccionado')

# ----------------------------
# HEADER / LOGO
# ----------------------------
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    st.image("TecLogo.png", width=300)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton+SC:wght@300;400;700&display=swap');
    .titulo {
        font-family: 'Anton SC', sans-serif;
        font-size: 60px;
        text-align: center;
        color: white;
    }
    .stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    <div class="titulo">GamesTEC</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center; color: gray;'>Bienvenido a la recopilación de juegos del TEC</h3>",
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------
# BOTÓN DE NAVEGACIÓN
# ----------------------------
col1, col2, col3 = st.columns([2, 2, 2])
with col2:
    if st.button("Ver Juegos con Descuentos"):
        st.switch_page("pages/Descuentos.py")

# ----------------------------
# ESTILOS GENERALES
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton+SC:wght@300;400;700&display=swap');

body {
    background-color: #1a1a1a;
    color: white;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Anton SC', sans-serif;
}

p, span, div, li, a {
    font-family: 'Bebas Neue', sans-serif;
}

.game-title {
    width: 100%;
    text-align: center;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.game-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# LISTA DE JUEGOS
# ----------------------------
st.subheader("Lista de Juegos")

num_columns = 4
columnas = st.columns(num_columns)
juegos = list(data.items())

for idx, (juego, detalles) in enumerate(juegos):
    col = columnas[idx % num_columns]
    imagen = imagenes.get(juego)

    with col:
        if imagen:
            st.markdown(
                f"<img src='{imagen}' class='game-image'>",
                unsafe_allow_html=True
            )

        st.markdown(
            f"<div class='game-title'>{juego.title()}</div>",
            unsafe_allow_html=True
        )

        if st.button("Ver Detalles", key=f"btn_{juego}"):
            plataformas = detalles.get("Plataformas y Precios", {})

            if "Xbox" in plataformas:
                plataformas["Xbox"]["GamePass"] = (
                    "Incluido en GamePass"
                    if plataformas["Xbox"].get("GamePass") is True
                    else "N/A"
                )

            st.session_state["juego_seleccionado"] = juego
            st.session_state["juego_detalles"] = detalles
            st.switch_page("pages/detalle_juego.py")

        st.write("---")
