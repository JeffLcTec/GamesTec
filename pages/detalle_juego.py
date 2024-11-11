import streamlit as st
import json

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
        font-weight: 400;
    }.game-image {
        width: 100%;
        height: 100px; /* Altura fija para las imágenes */
        object-fit: cover; /* Recorta los bordes para que la imagen se ajuste */
        border-radius: 8px; /* Bordes redondeados opcionales */
            
    }

    </style>
    """, unsafe_allow_html=True)
with open('imagenes.json', 'r') as file:
    imagenes = json.load(file)

# Mostrar detalles solo si hay un juego seleccionado
if 'juego_seleccionado' in st.session_state and 'juego_detalles' in st.session_state:
    
    juego = st.session_state['juego_seleccionado']
    detalles = st.session_state['juego_detalles']

    imagen = imagenes[juego.lower()]
    
    # Mostrar información del juego
    st.title(juego.title())
    if imagen:
            st.markdown(f"<img src='{imagen}' class='game-image' alt='Imagen del juego'>", unsafe_allow_html=True)
    st.subheader("Puntaje")
    st.write(f"- Critic Score: {detalles.get('Puntaje', {}).get('Critic score', 'N/A')}")
    st.write(f"- User Score: {detalles.get('Puntaje', {}).get('User Score', 'N/A')}")

    st.subheader("Plataformas y Precios")
    plataformas = detalles.get("Plataformas y Precios", {})

    for plataforma, precio_info in plataformas.items():
        color = {
            "Xbox": "#32CD32",     # Azul
            "PlayStation": "#001fff",  # Naranja
            "PC": "#1E90FF",       # Verde
            "Nintendo Switch": "ff0000",   # Rojo
            "Amazon" : "#FFD700" 
        }.get(plataforma, "#FFFFFF")  # Blanco por defecto si no coincide con ninguna
        precio_actual = precio_info.get("Precio Actual", 'N/A')
        descuento = precio_info.get("Descuento", 'N/A')
        if plataforma == "PlayStation":
            if precio_info.get('Oferta', 'N/A') == "Incluido":
                st.markdown(
                f"&bull;&nbsp;&nbsp;&nbsp;&nbsp; <span style='color:{color}; '> {plataforma}:</span> Incluido en PS PLUS",
                unsafe_allow_html=True
                )
            else:
                st.markdown(
                f"&bull;&nbsp;&nbsp;&nbsp;&nbsp; <span style='color:{color}; '> {plataforma}:</span> Precio Actual -<span style='color:#1d8348;'> {precio_info.get('Precio', 'N/A')}</span>, Descuento - <span style='color:#1d8348;'> {precio_info.get('Oferta', 'N/A')}",
                unsafe_allow_html=True
                )
        elif plataforma == "PC":
            st.markdown(
            f"&bull;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color:{color};'> {plataforma}:</span> Precio Actual -<span style='color:#1d8348;'> {precio_info.get('Precio', 'N/A')}</span> , Descuento - <span style='color:#1d8348;'> {precio_info.get('oferta', 'N/A')}",
            unsafe_allow_html=True
        )
        elif plataforma == "Amazon":
            st.markdown(
            f"&bull;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color:{color}; '> {plataforma}:</span> Precio Actual -<span style='color:#1d8348;'> {precio_info.get('Precio', 'N/A')}</span>",
            unsafe_allow_html=True
        )
        elif plataforma == "Xbox":
            st.markdown(
            f"&bull;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color:{color}; '> {plataforma}:</span> Precio Actual -<span style='color:#1d8348;'> {precio_info.get('Precio', 'N/A')}</span>, Descuento - <span style='color:#1d8348;'> {precio_info.get('GamePass', 'N/A')}",
            unsafe_allow_html=True
        )
        elif plataforma == "Nintendo Switch":
            st.markdown(
            f"&bull;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color:#FF6347;'> {plataforma}:</span> Precio Actual -<span style='color:#1d8348;'> {precio_info.get('Precio', 'N/A')}</span>, Descuento -<span style='color:#1d8348;'>  {precio_info.get('Oferta', 'N/A')}",
            unsafe_allow_html=True
        )

    st.subheader("How Long To Beat")
    for estilo, tiempo in detalles.get("How Long To Beat", {}).items():
        st.markdown(f"<span style='color:#d6eaf8; '>- {estilo}</span>: {tiempo}", unsafe_allow_html=True)
    
    # Botón para volver a la lista de juegos
    if st.button("Volver a la lista de juegos"):
        st.session_state.pop('juego_seleccionado', None)
        st.session_state.pop('juego_detalles', None)
        st.switch_page("Principal.py")  # Volver a la página principal
else:
    st.write("No hay un juego seleccionado. Vuelve a la lista de juegos.")
    if st.button("Volver a la lista de juegos"):
        st.session_state.pop('juego_seleccionado', None)
        st.session_state.pop('juego_detalles', None)
        st.switch_page("Principal.py")  # Volver a la página principal

