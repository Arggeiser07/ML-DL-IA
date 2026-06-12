import streamlit as st
from textblob import TextBlob
from textblob.exceptions import NotTranslated


def detect_and_translate(text: str) -> str:
    """Detecta el idioma del texto y lo traduce a inglés si no está ya en inglés."""
    blob = TextBlob(text)
    try:
        language = blob.detect_language()
    except Exception:
        return text

    if language != "en":
        try:
            translated = blob.translate(to="en")
            return str(translated)
        except NotTranslated:
            return text
        except Exception:
            return text
    return text


def analyze_sentiment(text: str) -> dict:
    translated_text = detect_and_translate(text)
    sentiment_blob = TextBlob(translated_text)
    sentiment = sentiment_blob.sentiment
    return {
        "original": text,
        "translated": translated_text,
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
    }


st.title("Análisis de sentimiento con Streamlit")
texto = st.text_area("Escribe un texto en español o inglés:")
if st.button("Analizar sentimiento"):
    if not texto.strip():
        st.warning("Por favor ingresa un texto para analizar.")
    else:
        resultado = analyze_sentiment(texto)
        st.write("**Texto original:**", resultado["original"])
        if resultado["translated"] != resultado["original"]:
            st.write("**Texto traducido a inglés:**", resultado["translated"])
        st.write("**Polaridad:**", resultado["polarity"])
        st.write("**Subjetividad:**", resultado["subjectivity"])
