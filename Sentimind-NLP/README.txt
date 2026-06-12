# 🧠 SentiMind - Analizador de Sentimientos Simple

Este es un proyecto sencillo de Procesamiento de Lenguaje Natural (NLP) que clasifica texto como positivo, negativo o neutro. Ideal para analizar reseñas, comentarios en redes sociales o feedback de usuarios.

## 🚀 Características
- **Análisis de Sentimiento:** Calcula la polaridad del texto (de -1 a 1).
- **Traducción Automática:** Capacidad para procesar texto en español traduciéndolo internamente a inglés para mayor precisión.
- **Interfaz Web:** Construido con Streamlit para una experiencia de usuario fluida.
- **Asistido por IA:** Desarrollado utilizando GitHub Copilot para optimizar el flujo de trabajo.

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **Streamlit:** Para la interfaz de usuario.
- **TextBlob:** Para el procesamiento de lenguaje natural y traducción.
- **Scikit-learn / Pandas:** (Opcional si decides escalar el proyecto).

## 📦 Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📝 Notas
Este proyecto fue realizado como una introducción al mundo del NLP, enfocándose en la integración de librerías de análisis léxico y el despliegue rápido de herramientas útiles.
