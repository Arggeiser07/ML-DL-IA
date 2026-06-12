"""Pipeline NLP básico con scikit-learn. El objetivo es mostrar cómo se puede construir un pipeline sencillo para análisis de sentimiento utilizando modelos preentrenados"""
""" [1. DATA] ──> [2. PREPROCESS] ──> [3. MODEL] ──> [4. EVALUATE/TRAIN] """
#0. Importaciones


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. CARGAR LOS DATOS (¿De dónde vienen?)
# Aquí importo mis textos y mis etiquetas.



X_train = [
    # Ejemplos Positivos (1)
    "Me encanta este producto, superó todas mis expectativas.",
    "El servicio al cliente fue rápido, amable y muy eficiente.",
    "Una experiencia maravillosa, definitivamente regresaré pronto.",
    "La calidad de los materiales es excelente por este precio.",
    "Funciona a la perfección y es muy fácil de usar.",
    "El envío llegó antes de tiempo y todo estaba perfecto.",
    "Es la mejor compra que he hecho en todo el año.",
    "Un diseño hermoso y muy cómodo en el día a día.",
    "Recomiendo totalmente este lugar, la comida es deliciosa.",
    "Cumple con todo lo prometido, estoy muy satisfecho.",
    
    # Ejemplos Negativos (0)
    "El producto llegó roto y la caja estaba aplastada.",
    "Pésimo servicio, nadie me quiso ayudar con mi problema.",
    "Una pérdida total de tiempo y dinero, no lo compren.",
    "La calidad es malísima, se rompió en el primer uso.",
    "No funciona bien, se traba a cada rato y es lento.",
    "El envío tardó un mes y encima llegó el color equivocado.",
    "Es el peor artículo que he comprado en mi vida.",
    "Muy incómodo de usar y las instrucciones no se entienden.",
    "La comida estaba fría y la atención fue muy grosera.",
    "No lo recomiendo para nada, es un engaño total."
]

y_train = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # 10 positivos
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0   # 10 negativos
]

frases_nuevas = [
    "El servicio fue un desastre total.",
    "Me pareció una maravilla de aparato."
]
# 2. PREPROCESAR (¿Cómo los preparo para la IA?)
# cargo pipeline de scikit-learn: vectorizer + modelo de clasifiación para este caso.
 
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()), #Vectorizer mas usado par texto con sklearn.
    ('classifier', LogisticRegression())
])

# 3. CONFIGURAR EL MODELO (¿Qué cerebro voy a usar?)
# Aquí importo el modelo de Hugging Face o scikit-learn ( ya se ha configurado al cargar el pipeline ).


# 4. ENTRENAR Y EVALUAR (¿Cómo sé si funciona?)
# Aquí ejecuto el bucle y mido el porcentaje de acierto (Accuracy).
pipeline.fit(X_train, y_train) #No se necesita variable
pipeline.predict(X_train )
accuracy = pipeline.score(X_train, y_train)
print(f"Accuracy: {accuracy:.2%}")



for frase in X_train:
    prediction = pipeline.predict([frase])[0]
    etiqueta = "Positivo" if prediction == 1 else "Negativo"
    print(f"Frase: {frase}")
    print(f"Predicción: {prediction} ({etiqueta})")
    print()



for frase in frases_nuevas:
    prediction = pipeline.predict([frase])[0]
    etiqueta = "Positivo" if prediction == 1 else "Negativo"
    print(f"Frase nueva: {frase}")
    print(f"Predicciones nuevas: {prediction} ({etiqueta})")
    print()


