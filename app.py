import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Super Rastreador de Compras",
    page_icon="🛒",
    layout="wide"
)

# Título principal
st.title("🛒 Super Rastreador de Compras: Meli, Shein, Temu & Amazon")
st.markdown("Tu panel unificado para buscar y comparar precios en las principales tiendas online.")

# Buscador General (arriba de todo para acceso rápido)
st.markdown("---")
st.subheader("🔍 Buscador General Unificado")
query_general = st.text_input("¿Qué producto estás buscando en todas las tiendas?", placeholder="Ej: zapatillas, campera, auricular bluetooth...")

if query_general:
    st.info(f"Buscando **'{query_general}'** en Mercado Libre, Shein, Temu y Amazon...")
    
    # Columnas de resultados para el buscador general
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 🟡 Mercado Libre")
        st.write(f"Resultados rápidos para *{query_general}*...")
        # Aquí puedes integrar la lógica de búsqueda de Meli que ya tenías
        st.link_button("Buscar en Meli", f"https://listado.mercadolibre.com.ar/{query_general}")
        
    with col2:
        st.markdown("### 🟣 Shein")
        st.write(f"Buscando en catálogo de Shein...")
        st.link_button("Buscar en Shein", f"https://us.shein.com/pdsearch/{query_general}")
        
    with col3:
        st.markdown("### 🟠 Temu")
        st.write(f"Buscando ofertas en Temu...")
        st.link_button("Buscar en Temu", f"https://www.temu.com/search_result.html?search_key={query_general}")
        
    with col4:
        st.markdown("### 🔵 Amazon")
        st.write(f"Buscando en Amazon...")
        st.link_button("Buscar en Amazon", f"https://www.amazon.com/s?k={query_general}")

st.markdown("---")

# Solapas o Secciones Separadas
tab_meli, tab_shein, tab_temu, tab_amazon = st.tabs([
    "🟡 Mercado Libre", 
    "🟣 Shein", 
    "🟠 Temu", 
    "🔵 Amazon"
])

with tab_meli:
    st.header("Panel Exclusivo - Mercado Libre Argentina")
    st.write("Acá podés gestionar tus búsquedas específicas, categorías y filtros de Mercado Libre.")
    # Pone aquí los componentes específicos que ya tenías hechos para Mercado Libre
    cat_meli = st.selectbox("Categorías Meli", ["Lo Más Comprado", "Ofertas del Día", "Tecnología", "Hogar"], key="meli_cat")

with tab_shein:
    st.header("Panel Exclusivo - Shein")
    st.write("Explorá tendencias, moda y accesorios de Shein.")
    cat_shein = st.selectbox("Categorías Shein", ["Moda Mujer", "Moda Hombre", "Hogar y Decó", "Accesorios"], key="shein_cat")

with tab_temu:
    st.header("Panel Exclusivo - Temu")
    st.write("Encontrá los mejores chiches, electrónica y novedades económicas de Temu.")
    cat_temu = st.selectbox("Categorías Temu", ["Más Vendidos", "Gadgets", "Herramientas", "Juguetes"], key="temu_cat")

with tab_amazon:
    st.header("Panel Exclusivo - Amazon")
    st.write("Revisá productos internacionales y tecnología importada desde Amazon.")
    cat_amazon = st.selectbox("Categorías Amazon", ["Electronics", "Computers", "Home & Kitchen", "Deals"], key="amazon_cat")
