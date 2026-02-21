import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import os
import base64

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="Dashboard de Talento", page_icon="✨", layout="wide")

# ==========================================
# ESTILOS CSS PERSONALIZADOS (Seguros)
# ==========================================
st.markdown("""
<style>
    .titulo-principal {
        font-size: 2.8rem;
        color: #1E3A8A;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 0px;
    }
    .subtitulo-principal {
        font-size: 1.3rem;
        color: #64748B;
        margin-top: 5px;
        margin-bottom: 30px;
    }
    .seccion-header {
        font-size: 1.6rem;
        color: #0F172A;
        border-bottom: 3px solid #3B82F6;
        padding-bottom: 8px;
        margin-top: 40px;
        margin-bottom: 20px;
        font-weight: 700;
    }
    .tarjeta {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #3B82F6;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        height: 100%;
    }
    .tarjeta-verde { border-left-color: #10B981; }
    .tarjeta-naranja { border-left-color: #F59E0B; }
    .tarjeta-morada { border-left-color: #8B5CF6; }
    .resultado-destacado {
        font-size: 1.4rem;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# FUNCIÓN PARA CARGAR LOS DATOS
# ==========================================
@st.cache_data
def cargar_datos():
    df = pd.read_excel("TEST streamlit.xlsx", sheet_name="BaseDatos")
    df = df.dropna(subset=['Nombre'])
    return df

try:
    df = cargar_datos()
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'TEST streamlit.xlsx'.")
    st.stop()


# ==========================================
# ENCABEZADO Y SELECTOR: LOGO SIN BOTONES + TÍTULO
# ==========================================
col_logo, col_titulo = st.columns([1, 5], gap="large")

with col_logo:
    if os.path.exists("logo.mp4"):
        with open("logo.mp4", "rb") as video_file:
            video_base64 = base64.b64encode(video_file.read()).decode()
        
        # Aislamos el HTML en un componente seguro para que no derrame texto
        # No usamos el atributo "controls", por lo que no habrá botones.
        video_html = f"""
        <style>
            body {{ margin: 0; padding: 0; overflow: hidden; background-color: transparent; }}
            video {{ width: 100%; max-height: 120px; object-fit: contain; pointer-events: none; border-radius: 10px; }}
        </style>
        <video autoplay loop muted playsinline>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """
        # Renderizamos el componente (caja fuerte)
        components.html(video_html, height=120, scrolling=False)
    else:
        st.warning("Sin logo")

with col_titulo:
    st.markdown('<div class="titulo-principal">✨ Perfil Integral de Talento</div>', unsafe_allow_html=True)
    
    # Selector de empleado
    nombres = df['Nombre'].unique().tolist()
    candidato_seleccionado = st.selectbox("🔎 Selecciona un perfil a analizar:", nombres, label_visibility="collapsed")

datos = df[df['Nombre'] == candidato_seleccionado].iloc[0]
st.markdown(f'<div class="subtitulo-principal">Analizando los resultados de: <b>{datos["Nombre"]}</b></div>', unsafe_allow_html=True)
st.markdown("---")


# ==========================================
# 1. ANCLAS DE CARRERA
# ==========================================
st.markdown('<div class="seccion-header">⚓ 1. Anclas de Carrera (Motivadores)</div>', unsafe_allow_html=True)

col_a1, col_a2, col_a3 = st.columns(3)

with col_a1:
    st.markdown(f'''
    <div class="tarjeta tarjeta-verde">
        <div class="resultado-destacado">🥇 1. {datos['Ancla 1']}</div>
        <p style="color: #475569; font-size: 0.95rem;">{datos['Desc Ancla 1']}</p>
    </div>
    ''', unsafe_allow_html=True)

with col_a2:
    st.markdown(f'''
    <div class="tarjeta tarjeta-verde">
        <div class="resultado-destacado">🥈 2. {datos['Ancla 2']}</div>
        <p style="color: #475569; font-size: 0.95rem;">{datos['Desc Ancla 2']}</p>
    </div>
    ''', unsafe_allow_html=True)

with col_a3:
    st.markdown(f'''
    <div class="tarjeta tarjeta-verde">
        <div class="resultado-destacado">🥉 3. {datos['Ancla 3']}</div>
        <p style="color: #475569; font-size: 0.95rem;">{datos['Desc Ancla 3']}</p>
    </div>
    ''', unsafe_allow_html=True)


# ==========================================
# 2. TEMPERAMENTO Y 3. MBTI
# ==========================================
st.markdown('<div class="seccion-header">🧠 2. Personalidad y Temperamento</div>', unsafe_allow_html=True)
col_temp, col_mbti = st.columns(2)

with col_temp:
    st.markdown(f'''
    <div class="tarjeta tarjeta-naranja">
        <h4 style="color: #F59E0B; margin-top:0;">🎭 Temperamento</h4>
        <div class="resultado-destacado">{datos['Temperamento']}</div>
        <p style="color: #475569; font-size: 0.95rem;">{datos['Desc Temp']}</p>
    </div>
    ''', unsafe_allow_html=True)

with col_mbti:
    st.markdown(f'''
    <div class="tarjeta tarjeta-morada">
        <h4 style="color: #8B5CF6; margin-top:0;">🧩 Perfil MBTI</h4>
        <div class="resultado-destacado">{datos['MBTI_1']}</div>
        <p style="color: #475569; font-size: 0.95rem;">{datos['MBTI_2']}</p>
    </div>
    ''', unsafe_allow_html=True)


# ==========================================
# 4. ESTILO DE LIDERAZGO
# ==========================================
st.markdown('<div class="seccion-header">🎯 4. Estilo de Liderazgo</div>', unsafe_allow_html=True)

st.markdown(f"**Estilo Dominante Identificado:** `{datos['Liderazgo']}`")

df_liderazgo = pd.DataFrame({
    "Estilos": [
        "Orientación al Resultado", 
        "Resultado y Personas", 
        "Orientación a las Personas", 
        "Sin Orientación"
    ],
    "Porcentaje": [
        datos['% Resultado'], 
        datos['% Resultado y Personas'], 
        datos['% Personas'], 
        datos['% Sin Orientacion']
    ]
})

fig = px.bar(
    df_liderazgo, 
    x="Porcentaje", 
    y="Estilos", 
    orientation='h',
    text="Porcentaje",
    color="Estilos",
    color_discrete_sequence=['#3B82F6', '#10B981', '#F59E0B', '#EF4444']
)

fig.update_traces(
    texttemplate='<b>%{text:.1%}</b>', 
    textposition='outside',
    textfont=dict(color='#0F172A', size=16),
    cliponaxis=False
)

fig.update_layout(
    template="plotly_white",
    showlegend=True,
    legend_title_text="Cuadrantes:",
    legend=dict(
        orientation="h",
        yanchor="bottom", y=1.05,
        xanchor="center", x=0.5,
        font=dict(size=14)
    ),
    xaxis=dict(range=[0, 1.15], title="", showticklabels=False),
    yaxis=dict(title="", showticklabels=False),
    margin=dict(l=0, r=0, t=20, b=0),
    height=450,
    bargap=0.15
)

st.markdown('<div style="background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #E2E8F0;">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><center><p style='color: #94A3B8;'>Dashboard interactivo generado automáticamente a partir de evaluaciones psicométricas.</p></center>", unsafe_allow_html=True)