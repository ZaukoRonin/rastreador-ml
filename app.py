import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Rastreador Mercado Libre Pro", page_icon="🛒", layout="wide"
)

st.title("🛒 Rastreador de Mercado Libre Argentina")
st.write(
    "Tu panel principal enfocado en encontrar los productos más comprados y"
    " las mejores ofertas."
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🏆 Lo Más Comprado y Ofertas",
        "⚡ Buscador de Ofertas",
        "📁 Categorías Rápidas",
        "💰 Filtrar por Presupuesto",
        "📊 Guardar y Exportar (CSV)",
    ]
)

with tab1:
    st.subheader(
        "🔥 Lo Más Comprado vs. ⚡ Mejores Ofertas (Panel Principal)"
    )
    st.write(
        "Accedé directamente a los listados principales donde se concentran"
        " las mayores ventas y descuentos del sitio."
    )

    col_1, col_2 = st.columns(2)

    with col_1:
        st.markdown("### 🏆 Los Más Comprados")
        st.write("Descubrí qué es lo que todo el mundo está comprando.")
        st.markdown(
            "👉 [Ver listado de Más Vendidos en Mercado"
            " Libre](https://www.mercadolibre.com.ar/mas-vendidos)",
            unsafe_allow_html=True,
        )

    with col_2:
        st.markdown("### ⚡ Las Mejores Ofertas")
        st.write("Encontrá descuentos imperdibles del día.")
        st.markdown(
            "👉 [Ver listado de Ofertas del Día en Mercado"
            " Libre](https://www.mercadolibre.com.ar/ofertas)",
            unsafe_allow_html=True,
        )

with tab2:
    st.subheader("⚡ Buscador Específico de Ofertas")
    st.write("Buscá un producto puntual y mirá sus ofertas vigentes.")

    prod_oferta = st.text_input(
        "¿Qué producto querés buscar en oferta?", "zapatillas"
    )

    if prod_oferta:
        prod_formateado = prod_oferta.replace(" ", "-")
        url_oferta = f"https://listado.mercadolibre.com.ar/{prod_formateado}_Dis_to_hasta_OFERTA"
        st.markdown(
            f"👉 [Ver ofertas de '{prod_oferta}' en Mercado"
            f" Libre]({url_oferta})",
            unsafe_allow_html=True,
        )

with tab3:
    st.subheader("📁 Categorías Rápidas (Filtradas en Oferta y Destacados)")
    st.write(
        "Elegí un rubro para ir directo a los productos con descuento de esa"
        " categoría:"
    )

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(
            "💻 [Celulares y Tecnología en"
            " Oferta](https://www.mercadolibre.com.ar/ofertas?category=MLA1051)",
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            "🏠 [Hogar y Muebles en"
            " Oferta](https://www.mercadolibre.com.ar/ofertas?category=MLA1574)",
            unsafe_allow_html=True,
        )
    with col_c:
        st.markdown(
            "🎮 [Consolas y Gaming en"
            " Oferta](https://www.mercadolibre.com.ar/ofertas?category=MLA1144)",
            unsafe_allow_html=True,
        )

with tab4:
    st.subheader("💰 Búsqueda con Rango de Presupuesto")
    p_busqueda = st.text_input(
        "Producto a buscar:", "auriculares inalambricos", key="p_busq"
    )
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        precio_min = st.number_input("Precio Mínimo ($)", min_value=0, value=5000)
    with col_p2:
        precio_max = st.number_input(
            "Precio Máximo ($)", min_value=0, value=50000
        )

    p_formateado = p_busqueda.replace(" ", "-")
    url_presupuesto = f"https://listado.mercadolibre.com.ar/{p_formateado}_PriceRange_{precio_min}-{precio_max}"

    st.markdown(
        f"👉 [Buscar '{p_busqueda}' entre ${precio_min} y ${precio_max}]"
        f"({url_presupuesto})",
        unsafe_allow_html=True,
    )

with tab5:
    st.subheader("📊 Exportar Listado Personalizado a CSV")
    datos_ejemplo = {
        "Producto": [
            "Auriculares Gamer",
            "Zapatillas Nike",
            "Teclado Mecánico",
        ],
        "Precio Estimado": [15000, 45000, 22000],
        "Categoría": ["Tecnología", "Calzada", "Tecnología"],
    }
    df = pd.DataFrame(datos_ejemplo)

    st.write("Vista previa de tus productos guardados:")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar lista en CSV",
        data=csv,
        file_name="mis_productos_mercadolibre.csv",
        mime="text/csv",
    )