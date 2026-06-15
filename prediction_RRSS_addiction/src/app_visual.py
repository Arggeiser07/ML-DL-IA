import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import pickle
import sys
from sklearn.linear_model import LinearRegression
sys.modules['LinearRegression'] = LinearRegression

# Configuración de la página web
st.set_page_config(page_title="Addiction-score(prueba)", page_icon="📊", layout="centered")

# Título y diseño con colores
st.title("📊 Sistema Predictivo de Análisis de Adicciones")
st.markdown("Mueve las barras deslizantes para evaluar el riesgo en tiempo real.")
st.write("---")

# 1. Cargar el modelo de forma limpia
@st.cache_resource  # Esto hace que el modelo se cargue una sola vez en memoria y vaya ultrasónico
def cargar_modelo():
   # Creamos un objeto limpio de la versión actual de Docker
    model = LinearRegression()
    
    # Le inyectamos directamente TUS datos reales de Jupyter
    model.intercept_ = 0.821917843361625  # <-- Pega aquí el número de Intercept (ej: 3.1416)
    model.coef_ = np.array([
        4.93150684e-02,
        4.93150684e-02,
        -8.21917807e-03,
        -4.28307401e-09,
        5.00000000e-01,
        -2.18390750e-10 ]) # <-- Pega aquí la lista de coeficientes separados por comas
    
    # Le decimos a scikit-learn cuántas variables de entrada espera
    model.n_features_in_ = len(model.coef_)
    return model

model = cargar_modelo()

# 2. Creación de Sliders y componentes interactivos en la web
st.subheader("📝 Introducción de Variables del Usuario")

tiktok = st.slider("Minutos diarios en TikTok:", min_value=0, max_value=480, value=60, step=5)
instagram = st.slider("Minutos diarios en Instagram:", min_value=0, max_value=480, value=45, step=5)
attention = st.slider("Puntuación de Capacidad de Atención (Score):", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sleep = st.slider("Horas de Sueño Diarias:", min_value=0.0, max_value=12.0, value=7.0, step=0.5)
asi = st.number_input("Índice ASI (Addiction Severity Index):", min_value=0, max_value=50, value=10)
mhri = st.number_input("Índice MHRI (Mental Health Risk Index):", min_value=0, max_value=100, value=25)

st.write("---")

# 3. Botón para ejecutar la predicción
if st.button("🔮 Calcular Predicción de Riesgo", use_container_width=True):
    # Crear el DataFrame con los nombres de columnas EXACTOS
    features = {
        'tiktok_minutes_daily': [tiktok],
        'instagram_minutes_daily': [instagram],
        'attention_span_score': [attention],
        'sleep_hours': [sleep],
        'ASI': [asi],
        'MHRI': [mhri]
    }
    df_input = pd.DataFrame(features)
    
    # Realizar la predicción
    prediccion = model.predict(df_input)[0]
    
    # 4. Mostrar el resultado con alertas de colores visuales
    st.subheader("🎯 Resultado de la Evaluación:")
    
    if prediccion == 1:  # Asumiendo que 1 es Riesgo Alto
        st.error(f"⚠️ **Riesgo Alto Detectado** (Clase: {prediccion})")
        st.progress(100) # Barra de progreso visual en rojo
    else:
        st.success(f"✅ **Riesgo Bajo / Controlado** (Clase: {prediccion})")
        st.progress(25)  # Barra de progreso visual en verde