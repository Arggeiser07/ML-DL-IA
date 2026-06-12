"""
Proyecto: Pipeline Base de NLP - Análisis de Sentimiento
Autor: [Rafa GL]
Descripción: Un pipeline básico que toma texto crudo, lo procesa usando 
             modelos preentrenados de Hugging Face y muestra los resultados.
"""

# ==========================================
# 1. IMPORTACIONES
# ==========================================
# TODO: Importar la función 'pipeline' de la librería transformers
from transformers import pipeline


# ==========================================
# 2. CONFIGURACIÓN DE DATOS
# ==========================================
# TODO: Crear una lista llamada 'textos_ejemplo' con 3 frases (2 positivas, 1 negativa)
textos = ["Estoy ilusinado con este proyecto, aunque es muy ambicioso",
          "La IA es fascinante, pero hay que tener cuidado con su uso",
          "Me encanta la complejidad de los modelos... parecían sencillos"]

texto_prueba = "El diseño del nuevo dispositivo es una absoluta maravilla y se siente muy premium en la mano; sin embargo, la batería dura apenas un par de horas y el software se cierra inesperadamente todo el tiempo, lo cual resulta extremadamente frustrante."


# ==========================================
# 3. CARGA DEL MODELO
# ==========================================
# TODO: Inicializar pipeline con task + modelo de Hugging Face
pipeline_es = pipeline(task="sentiment-analysis", model="pysentimiento/roberta-es-sentiment") #Modelo en español


# ==========================================
# 4. EJECUCIÓN Y EVALUACIÓN (PIPELINE)
# ==========================================
# TODO: Recorrer la lista con un bucle for, pasar cada texto al modelo e imprimir el resultado
for frase in textos:
    resultado = pipeline_es(frase)
    resultado[0]['score'] = round(resultado[0]['score'], 3)#Redondeo a 3 cifras, por defecto da demasiadas.
    print(f"Texto: {frase}\nResultado: {resultado}\n{'-'*40}")

# TODO: Pasar el texto de prueba al modelo e imprimir el resultado
resultado_prueba = pipeline_es(texto_prueba)
resultado_prueba[0]['score'] = round(resultado_prueba[0]['score'], 3)
print(f"Texto de prueba: {texto_prueba}\nResultado: {resultado_prueba}\n{'-'*40}")
    