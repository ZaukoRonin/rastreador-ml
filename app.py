import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Super Rastreador de Compras",
    page_icon="🛒",
    layout="wide"
)

# Título principal
st.title("🛒 Super Rastreador de Compras: Meli, Shein, Temu & Amazon")
st.markdown("Tu panel unificado para buscar y comparar precios en las 4 tiendas simultáneamente.")

# Buscador General Unificado (Muestra las 4 tiendas juntas en columnas a la vez)
st.markdown("---")
st.subheader("🔍 Buscador General (Resultados en 4 columnas simultáneas)")
query_general = st.text_input("¿Qué producto querés buscar en las 4 tiendas a la vez?", placeholder="Ej: zapatillas, campera, auricular bluetooth...")

if query_general:
    st.markdown(f"### 🎯 Buscando **'{query_general}'** en simultáneo:")
    
    # Creamos 4 columnas para ver las 4 tiendas lado a lado en la misma pantalla
    col1, col2, col3, col4 = st.columns(4)
    
    url_q = query_general.replace(' ', '-')
    
    with col1:
        st.markdown("### 🟡 Mercado Libre")
        st.info("Búsqueda directa en Argentina")
        st.link_button("Abrir Meli con esto", f"https://listado.mercadolibre.com.ar/{url_q}", use_container_width=True)
        
    with col2:
        st.markdown("### 🟣 Shein")
        st.info("Búsqueda directa en Shein")
        st.link_button("Abrir Shein con esto", f"https://us.shein.com/pdsearch/{query_general.replace(' ', '%20')}", use_container_width=True)
        
    with col3:
        st.markdown("### 🟠 Temu")
        st.info("Búsqueda directa en Temu")
        st.link_button("Abrir Temu con esto", f"https://www.temu.com/search_result.html?search_key={query_general.replace(' ', '%20')}", use_container_width=True)
        
    with col4:
        st.markdown("### 🔵 Amazon")
        st.info("Búsqueda directa en Amazon")
        st.link_button("Abrir Amazon con esto", f"https://www.amazon.com/s?k={query_general.replace(' ', '+')}", use_container_width=True)

st.markdown("---")

# Solapas principales para explorar cada tienda por separado y sus categorías
tab_meli, tab_shein, tab_temu, tab_amazon = st.tabs([
    "🟡 Mercado Libre", 
    "🟣 Shein", 
    "🟠 Temu", 
    "🔵 Amazon"
])

with tab_meli:
    st.header("🟡 Mercado Libre Argentina")
    sub_t1, sub_t2 = st.tabs(["🔥 Lo Más Comprado y Ofertas", "📂 Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Ver Más Vendidos", "https://www.mercadolibre.com.ar/mas-vendidos", use_container_width=True)
        with c2:
            st.link_button("Ver Ofertas del Día", "https://www.mercadolibre.com.ar/ofertas", use_container_width=True)
    with sub_t2:
        cat_meli = st.selectbox("Categorías Meli:", ["Tecnología", "Hogar y Muebles", "Ropa y Accesorios", "Deportes"], key="m_cat")
        st.link_button(f"Buscar '{cat_meli}'", f"https://listado.mercadolibre.com.ar/{cat_meli.lower()}", use_container_width=True)

with tab_shein:
    st.header("🟣 Shein")
    sub_t1, sub_t2 = st.tabs(["🔥 Tendencias y Ofertas", "📂 Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Ver Tendencias", "https://us.shein.com/campaign/topsellers", use_container_width=True)
        with c2:
            st.link_button("Ver Flash Sale", "https://us.shein.com/flash-sale.html", use_container_width=True)
    with sub_t2:
        cat_shein = st.selectbox("Categorías Shein:", ["Moda Mujer", "Moda Hombre", "Hogar", "Belleza"], key="s_cat")
        st.link_button(f"Buscar '{cat_shein}'", f"https://us.shein.com/pdsearch/{cat_shein.lower()}", use_container_width=True)

with tab_temu:
    st.header("🟠 Temu")
    sub_t1, sub_t2 = st.tabs(["🔥 Más Vendidos y Ofertas", "📂 Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Ver Más Vendidos", "https://www.temu.com/best-sellers.html", use_container_width=True)
        with c2:
            st.link_button("Ver Ofertas", "https://www.temu.com/lightning-deals.html", use_container_width=True)
    with sub_t2:
        cat_temu = st.selectbox("Categorías Temu:", ["Gadgets", "Hogar", "Herramientas", "Juguetes"], key="t_cat")
        st.link_button(f"Buscar '{cat_temu}'", f"https://www.temu.com/search_result.html?search_key={cat_temu.lower()}", use_container_width=True)

with tab_amazon:
    st.header("🔵 Amazon")
    sub_t1, sub_t2 = st.tabs(["🔥 Best Sellers y Deals", "📂 Categorías"])
    with sub_t1:
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Ver Best Sellers", "https://www.amazon.com/gp/bestsellers", use_container_width=True)
        with c2:
            st.link_button("Ver Today's Deals", "https://www.amazon.com/gp/goldbox", use_container_width=True)
    with sub_t2:
        cat_amazon = st.selectbox("Categorías Amazon:", ["Electronics", "Computers", "Home & Kitchen", "Video Games"], key="a_cat")
        st.link_button(f"Buscar '{cat_amazon}'", f"https://www.amazon.com/s?k={cat_amazon.lower()}", use_container_width=True)
