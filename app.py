import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Super Rastreador de Compras",
    page_icon="🛒",
    layout="wide"
)

# Título principal
st.title("🛒 Super Rastreador de Compras: Meli, Shein, Temu & Amazon")
st.markdown("Tu panel unificado para buscar y comparar precios en las 4 tiendas.")

# Buscador General Unificado
st.markdown("---")
st.subheader("🔍 Buscador General Unificado")
query_general = st.text_input("¿Qué producto querés buscar en las 4 tiendas a la vez?", placeholder="Ej: zapatillas, campera, auricular bluetooth...")

if query_general:
    st.markdown(f"### 🎯 Buscando **'{query_general}'** en simultáneo:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 🟡 Mercado Libre")
        st.link_button("Buscar en Meli", f"https://listado.mercadolibre.com.ar/{query_general.replace(' ', '-')}", use_container_width=True)
        
    with col2:
        st.markdown("### 🟣 Shein")
        st.link_button("Buscar en Shein", f"https://us.shein.com/pdsearch/{query_general.replace(' ', '%20')}", use_container_width=True)
        
    with col3:
        st.markdown("### 🟠 Temu")
        st.link_button("Buscar en Temu", f"https://www.temu.com/search_result.html?search_key={query_general.replace(' ', '%20')}", use_container_width=True)
        
    with col4:
        st.markdown("### 🔵 Amazon")
        st.link_button("Buscar en Amazon", f"https://www.amazon.com/s?k={query_general.replace(' ', '+')}", use_container_width=True)

st.markdown("---")

# Lista unificada de categorías
categorias_comunes = [
    "Ropa Mujer", 
    "Ropa Hombre", 
    "Ropa Niño", 
    "Hogar y Decoración", 
    "Tecnología y Electrónica", 
    "Cosméticos y Belleza", 
    "Calzado y Accesorios", 
    "Deportes y Aire Libre"
]

# Solapas principales para cada tienda
tab_meli, tab_shein, tab_temu, tab_amazon = st.tabs([
    "🟡 Mercado Libre", 
    "🟣 Shein", 
    "🟠 Temu", 
    "🔵 Amazon"
])

# --- SOLAPA MELI ---
with tab_meli:
    st.header("🟡 Mercado Libre Argentina")
    sub_t1, sub_t2 = st.tabs(["🔥 Lo Más Comprado y Ofertas", "📂 Explorar Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Ver Más Vendidos", "https://www.mercadolibre.com.ar/mas-vendidos", use_container_width=True)
        with c2:
            st.link_button("Ver Ofertas del Día", "https://www.mercadolibre.com.ar/ofertas", use_container_width=True)
    with sub_t2:
        cat_meli = st.selectbox("Elegí una categoría en Meli:", categorias_comunes, key="m_cat")
        st.link_button(f"Buscar '{cat_meli}' en Meli", f"https://listado.mercadolibre.com.ar/{cat_meli.lower().replace(' ', '-')}", use_container_width=True)

# --- SOLAPA SHEIN ---
with tab_shein:
    st.header("🟣 Shein")
    sub_t1, sub_t2 = st.tabs(["🔥 Lo Más Popular y Ofertas", "📂 Explorar Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            # Enlace directo a Novedades/Populares de Shein (como la captura 4)
            st.link_button("Ver Más Populares / Novedades", "https://us.shein.com/recommend/New-In-c-1799.html", use_container_width=True)
        with c2:
            st.link_button("Ver Ofertas Flash", "https://us.shein.com/flash-sale.html", use_container_width=True)
    with sub_t2:
        cat_shein = st.selectbox("Elegí una categoría en Shein:", categorias_comunes, key="s_cat")
        st.link_button(f"Buscar '{cat_shein}' en Shein", f"https://us.shein.com/pdsearch/{cat_shein.lower().replace(' ', '%20')}", use_container_width=True)

# --- SOLAPA TEMU ---
with tab_temu:
    st.header("🟠 Temu")
    sub_t1, sub_t2 = st.tabs(["🔥 Lo Más Comprado y Ofertas", "📂 Explorar Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            # Enlace directo a Artículos más vendidos de Temu (como la captura 3)
            st.link_button("Ver Más Vendidos", "https://www.temu.com/ar/channel/best-sellers.html", use_container_width=True)
        with c2:
            st.link_button("Ver Ofertas Relámpago", "https://www.temu.com/lightning-deals.html", use_container_width=True)
    with sub_t2:
        cat_temu = st.selectbox("Elegí una categoría en Temu:", categorias_comunes, key="t_cat")
        st.link_button(f"Buscar '{cat_temu}' en Temu", f"https://www.temu.com/search_result.html?search_key={cat_temu.lower().replace(' ', '%20')}", use_container_width=True)

# --- SOLAPA AMAZON ---
with tab_amazon:
    st.header("🔵 Amazon")
    sub_t1, sub_t2 = st.tabs(["🔥 Lo Más Comprado y Ofertas", "📂 Explorar Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Ver Best Sellers", "https://www.amazon.com/gp/bestsellers", use_container_width=True)
        with c2:
            st.link_button("Ver Today's Deals", "https://www.amazon.com/gp/goldbox", use_container_width=True)
    with sub_t2:
        cat_amazon = st.selectbox("Elegí una categoría en Amazon:", categorias_comunes, key="a_cat")
        st.link_button(f"Buscar '{cat_amazon}' en Amazon", f"https://www.amazon.com/s?k={cat_amazon.lower().replace(' ', '+')}", use_container_width=True)
