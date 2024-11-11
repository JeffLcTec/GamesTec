import streamlit as st
import pandas as pd
import json
import requests
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import json
import os


# Inicializa Firebase con tu archivo de credenciales
if not firebase_admin._apps:
    cred = credentials.Certificate("arqui-a68cb-firebase-adminsdk-wvdaf-5b49548963.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://arqui-a68cb-default-rtdb.firebaseio.com/'
    })

# with open("juegosjson.json", 'r') as archivo:
#     juegos = json.load(archivo)

# ref = db.reference("Lista de juegos")
# ref.set(juegos)

ref = db.reference("Juegos Actualizados")
datos = ref.get()

with open("JuegosActualizado.json", 'w') as archivo:
    json.dump(datos, archivo, indent=4)

# Configuración de página principal
col1, col2, col3 = st.columns([2, 1, 2])  # Columnas con proporciones 1:2:1
with col2:
    st.image("TecLogo.png", width=300) 

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton+SC:wght@300;400;700&display=swap');
    .titulo {
        font-family: 'Anton SC', sans-serif;
        font-size: 60px;
        font-weight: 400;
        text-align: center;
        color: "white";
    }.stButton > button {
        display: block;
        margin: 0 auto;
    }
    
    </style>
    <div class="titulo">
        GamesTEC
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<h3 style='text-align: center; color: gray;'>Bienvenido a la recopilación de juegos del TEC</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)  # Añadir saltos de línea


col1, col2, col3 = st.columns([2, 2, 2])

with col2:
    if st.button('Ver Juegos con Descuentos'):
        st.switch_page("pages/Descuentos.py")
# Estilo CSS personalizado para darle un toque adicional
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: white;
    }
    h1, h3 {
        font-family: 'Arial', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)
# Cargar datos del archivo JSON
with open('JuegosActualizado.json', 'r') as file:
    data = json.load(file)
with open('imagenes.json', 'r') as file:
    imagenes = json.load(file)
if 'juego_seleccionado' in st.session_state:
    st.session_state.pop('juego_seleccionado')




st.markdown("""
    <style>
            /* Importar Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Anton+SC:wght@300;400;700&display=swap');
    /* Cambiar la fuente de los títulos */
    h1, h2, h3, h4, h5, h6{
        font-family: 'Anton SC', sans-serif;
        font-weight: 400;
    }

    /* Cambiar la fuente del texto general */
    p, span, div, li, a  {
        font-family: 'bebas Neue', sans-serif;
        font-weight: 150;
    }
    .game-title {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        display: flex;
        text-align: center;
        justify-content: center
        
    }
    .game-image {
        width: 100%;
        height: 150px; /* Altura fija para las imágenes */
        object-fit: cover; /* Recorta los bordes para que la imagen se ajuste */
        border-radius: 8px; /* Bordes redondeados opcionales */
            
    }
    </style>
    """, unsafe_allow_html=True)



# Mostrar lista de juegos y sus detalles
st.subheader("Lista de Juegos")

num_columns = 4
columnas = st.columns(num_columns)

# Crear una lista con los datos de cada juego
juegos = list(data.items())

for idx, (juego, detalles) in enumerate(juegos):
    col = columnas[idx % num_columns]
    imagen = imagenes[juego]
    with col:
        if imagen:
            st.markdown(f"<img src='{imagen}' class='game-image' alt='Imagen del juego'>", unsafe_allow_html=True)
          # Coloca el nombre del juego en un contenedor independiente
        
        
        st.markdown(f"<div class='game-title'>{juego.title()}</div>", unsafe_allow_html=True)
        if st.button(f"Ver Detalles", key=f"btn_{juego}", help=juego.title()):
            plataformas = detalles.get("Plataformas y Precios", {})

            for plataforma, precio_info in plataformas.items():
                if plataforma == "Xbox":
                    if detalles["Plataformas y Precios"][plataforma]["GamePass"] == True:
                        detalles["Plataformas y Precios"]["Xbox"]["GamePass"] = "Incluido en GamePass"
                    else:
                        detalles["Plataformas y Precios"]["Xbox"]["GamePass"] = "N/A"
            # Almacenar el juego seleccionado en session_state
            st.session_state['juego_seleccionado'] = juego
            st.session_state['juego_detalles'] = detalles  
            st.switch_page("pages/detalle_juego.py")
        st.write("---")
        st.markdown("<br>", unsafe_allow_html=True)  # Espacio más grande


