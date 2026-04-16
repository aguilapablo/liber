import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Liber S.A. | Escisión Art. 80 LIG", layout="wide")

st.markdown("""
<div style="background-color:#0d2b4e; color:white; padding:25px; border-radius:12px; text-align:center;">
    <h1 style="margin:0;">Liber S.A.</h1>
    <h2 style="margin:8px 0 20px 0;">Escisión Estratégica Libre de Impuestos 2026</h2>
    <p style="font-size:20px; margin:0;"><strong>Tablero de Comando Directivo</strong></p>
    <p style="margin:12px 0 0 0;">Realizado con Lic. Pablo Aguila<br>
    Administración y Estrategia | Abril 2026</p>
</div>
""", unsafe_allow_html=True)

st.caption("Herramienta Directiva, Operativa y Gerencial – Art. 80 LIG")

# ====================== CONTROLES ======================
st.subheader("🔧 Capitalización de Gastos por Sociedad (RT 17)")
col1, col2, col3 = st.columns(3)
with col1:
    mejoras_pama = st.slider("PAMA", 0, 12_000_000, 5_982_757, 50_000)
with col2:
    mejoras_nbr = st.slider("NBR", 0, 8_000_000, 0, 50_000)
with col3:
    mejoras_vifran = st.slider("VIFRAN", 0, 10_000_000, 2_587_693, 50_000)

st.subheader("Ajustes Regulatorios")
col_a, col_b = st.columns(2)
with col_a:
    valor_mercado_malabia = st.slider("Valor real de mercado Malabia", 200_000_000, 452_000_000, 300_000_000, 1_000_000)
with col_b:
    tasa_bna = st.slider("Tasa Pasiva BNA anual (%)", 20.0, 80.0, 45.0, 0.5)

# ====================== CÁLCULOS ======================
base_inmuebles = {"PAMA": 23625635.52, "NBR": 46275617.63, "VIFRAN": 50531055.73}

pn = {
    "PAMA": base_inmuebles["PAMA"] + mejoras_pama,
    "NBR": base_inmuebles["NBR"] + mejoras_nbr,
    "VIFRAN": base_inmuebles["VIFRAN"] + mejoras_vifran
}

pn_total_calculado = sum(pn.values())
ajuste = 132796868 - pn_total_calculado

pn["PAMA"] += ajuste * 0.30
pn["NBR"] += ajuste * 0.30
pn["VIFRAN"] += ajuste * 0.40

# Cálculo trimestral BNA
capital_original = 72900000
fecha_origen = datetime(2023, 1, 1)
fecha_cierre = datetime(2026, 7, 31)
dias_totales = (fecha_cierre - fecha_origen).days
trimestres = dias_totales / 91.25
tasa_trimestral = tasa_bna / 4
intereses = capital_original * (tasa_trimestral / 100) * trimestres
pasivo_actualizado = capital_original + intereses

# ====================== MAPA DE INMUEBLES ======================
st.subheader("🗺️ Mapa de Inmuebles por Sociedad")
col1, col2, col3 = st.columns(3)
with col1:
    st.sub
