#Imports + configuración de entorno
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from newspaper import Article
import nltk

# Descargas necesarias para procesamiento de texto (puntuación del texto, donde empieza y termina cada frase).
nltk.download('punkt', quiet=True)

def check_env():
    print(f"🚀 Torch versión: {torch.__version__}")
    print(f"✅ Dispositivo detectado: {'cuda' if torch.cuda.is_available() else 'cpu'}")

check_env()

# MÓDULO 2: Extracción de noticias
def extraer_noticia(url):
    try:
        article = Article(url, language='es')
        article.download()
        article.parse()
        
        # Diccionario con la data limpia
        noticia = {
            "titulo": article.title,
            "texto": article.text,
            "fecha": article.publish_date
        }
        
        if len(noticia["texto"]) < 100:
            print("⚠️ Advertencia: El texto extraído es muy corto.")
            
        return noticia

    except Exception as e:
        print(f"❌ Error al extraer la noticia: {e}")
        return None

# --- PRUEBA DE Extracción ---
test_url = "https://motor.elpais.com/coches-electricos/el-byd-seal-sigue-siendo-la-misma-berlina-electrica-de-hasta-530-cv-pero-ahora-tiene-un-25-mas-de-maletero/" # Usa una URL real
data = extraer_noticia(test_url)

if data:
    print(f"\n📰 Título: {data['titulo']}")
    print(f"📝 Fragmento: {data['texto'][:150]}...")

# Definimos el ID del modelo (puedes probar otros luego)

MODEL_NAME = "Narrativa/bsc_roberta2roberta_shared-spanish-finetuned-mlsum-summarization"




def cargar_ia():
    print(f"⏳ Cargando modelo: {MODEL_NAME}...")
    try:
        # Cargamos el tokenizador
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        
        # Cargamos el modelo y lo movemos a GPU si está disponible
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device)
        
        # ESTO ES CLAVE PARA MBART:
        if "mbart" in MODEL_NAME.lower():
            tokenizer.src_lang = "es_XX"
        
        print("✅ IA cargada correctamente.")
        return tokenizer, model, device

    except Exception as e:
        print(f"❌ Error al cargar la IA: {e}")
        return None, None, None

# --- PRUEBA DEL MÓDULO 3 ---
tokenizer, model, device = cargar_ia()

#Función para generar resúmenes detallados usando el modelo cargado ( inferencia )
def generar_resumen(texto, tokenizer, model, device):
    try:
        # 1. Tokenización simple
        # Forzamos a que devuelva tensores de PyTorch ('pt')
    
        inputs = tokenizer(texto, return_tensors="pt", max_length=512, truncation=True).to(device)

        # 3. Generación directa
        # Pasamos los tensores desempaquetados con **
        outputs = model.generate(
            **inputs, # Esto pasa input_ids y attention_mask correctamente
            max_length=250, 
            min_length=100, 
            num_beams=5,
            length_penalty=1.5,
            no_repeat_ngram_size=3,
            repetition_penalty=2.5,
            early_stopping=True
        )

        # 4. Decodificación limpia
        # [0] asegura que tomamos la primera (y única) respuesta generada
        resumen = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return resumen

    except Exception as e:
        return f"❌ Error en la generación: {e}"

# --- PRUEBA FINAL: UNIENDO TODO ---
if data and model:
    print("\n" + "="*30)
    print("🤖 GENERANDO RESUMEN DETALLADO...")
    print("="*30)
    
    resultado = generar_resumen(data['texto'], tokenizer, model, device)
    
    print(f"\n📝 RESUMEN FINAL:\n{resultado}")

import gradio as gr

def proceso_completo(url):
    # 1. Extraer la noticia (Módulo 2)
    datos = extraer_noticia(url)
    if not datos:
        return "❌ Error: No se pudo extraer el texto de esta URL."
    
    # 2. Generar el resumen (Módulo 4)
    # Usamos el modelo Narrativa que encontraste
    resumen = generar_resumen(datos['texto'], tokenizer, model, device)
    
    # 3. Formatear la salida para la interfaz
    return f"📌 TÍTULO: {datos['titulo']}\n\n📝 RESUMEN:\n{resumen}"

# --- CONFIGURACIÓN DE LA INTERFAZ ---
demo = gr.Interface(
    fn=proceso_completo, 
    inputs=gr.Textbox(label="Pega aquí la URL de la noticia", placeholder="https://elpais.com..."),
    outputs=gr.Textbox(label="NotiBrief: Resumen Detallado", lines=10),
    title="🚀 NotiBrief: Tu Resumidor de Noticias con IA",
    description="Extrae y resume noticias en español usando modelos avanzados de Transformers.",
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()
