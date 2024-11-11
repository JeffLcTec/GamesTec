import streamlit as st
import json


# Cargar datos desde el archivo JSON
with open('JuegosActualizado.json', 'r') as file:
    data = json.load(file)

with open('imagenes.json', 'r') as file:
    imagenes = json.load(file)
st.title("Lista de Juegos con Descuento")

# Crear una lista filtrada para juegos con descuento
juegos_con_descuento = {juego: detalles for juego, detalles in data.items()
    if any((precio_info.get("oferta") not in (None, "Sin descuento") or precio_info.get("Oferta") not in (None, "Sin descuento") or precio_info.get("GamePass") == True) for precio_info in detalles.get("Plataformas y Precios", {}).values()
    )
}
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
        
    }
    .game-image {
        width: 100%;
        height: 150px; /* Altura fija para las imágenes */
        object-fit: cover; /* Recorta los bordes para que la imagen se ajuste */
        border-radius: 8px; /* Bordes redondeados opcionales */
            
    }
    </style>
    """, unsafe_allow_html=True)


num_columns = 4
columnas = st.columns(num_columns)

# Mostrar lista de juegos con descuento
if juegos_con_descuento:
    for idx,(juego, detalles) in enumerate(juegos_con_descuento.items()):
        col = columnas[idx % num_columns]
        imagen = imagenes[juego]
        juego = juego.title()
        with col:
            if imagen:
                st.markdown(f"<img src='{imagen}' class='game-image' alt='Imagen del juego'>", unsafe_allow_html=True)
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
else:
    st.write("No hay juegos con descuento en este momento.")

