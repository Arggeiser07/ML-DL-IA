import os
import joblib
import pandas as pd
from typing import Dict, List

# 1. CONFIGURACIÓN Y CARGA DE ARTIFACTS
# Cargamos el archivo completo que contiene el modelo y sus columnas
MODEL_PATH = (r"src\modelo_completo.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"No se encuentra el archivo {MODEL_PATH}. ¿Lo exportaste bien desde el cuaderno?")

# Cargamos el diccionario empaquetado
assets_modelo = joblib.load(MODEL_PATH)
model = assets_modelo['modelo']
FEATURES_OBLIGATORIAS = assets_modelo['features']


# 2. FUNCIÓN DE PREDICCIÓN (La lógica de negocio)
def predecir_score_adiccion(datos_registro: Dict[str, float]) -> float:
    """
    Recibe un diccionario con los datos de un nuevo registro,
    lo valida, lo transforma a DataFrame y devuelve la predicción del score.
    """
    # Convertimos el diccionario a DataFrame de Pandas (un único registro)
    df_nuevo = pd.DataFrame([datos_registro])
    
    # Validamos que el orden y las columnas sean exactamente las que el modelo espera
    try:
        df_nuevo = df_nuevo[FEATURES_OBLIGATORIAS]
    except KeyError as e:
        raise ValueError(f"Faltan variables obligatorias en los datos de entrada. Detalle: {e}")
    
    # Ejecutamos la "fórmula" guardada
    prediccion = model.predict(df_nuevo)
    
    # Devolvemos el número directo (el primer elemento del array de salida)
    return float(prediccion[0])

def solicitar_datos_usuario(features_necesarias: List[str]) -> Dict[str, float]:
    """
    Pide al usuario por consola el valor de cada feature una a una,
    valida que sea un número y devuelve el diccionario listo para el modelo.
    """
    print("\n--- INTRODUCCIÓN DE NUEVO REGISTRO ---")
    print("Por favor, introduce los valores numéricos para las siguientes variables:")
    
    registro_nuevo = {}
    
    for feature in features_necesarias:
        while True:
            try:
                # Pedimos el dato dinámicamente usando el nombre de la feature
                valor_input = input(f"➔ {feature}: ")
                
                # Lo convertimos a float (ya que el modelo espera números decimales)
                valor_numerico = float(valor_input)
                
                # Guardamos en el diccionario con su clave correspondiente
                registro_nuevo[feature] = valor_numerico
                break  # Si todo ha ido bien, salimos del bucle interno y pasamos a la siguiente feature
                
            except ValueError:
                print(f"⚠️ Error: El valor para '{feature}' debe ser un número válido (ej: 4 o 3.5). Inténtalo de nuevo.")
                
    return registro_nuevo


# 3. PUNTO DE ENTRADA A LA APLICACIÓN
if __name__ == "__main__":
    print("=== SERVICIO DE PREDICCIÓN INICIALIZADO ===")
    print(f"Features que va a exigir el modelo : {FEATURES_OBLIGATORIAS}\n")
    
    # Simulación de un nuevo registro que entra al sistema (por ejemplo, id_usuario: 402)
    # NOTA: Rellena este diccionario con los nombres exactos que te salieron en X.columns
    datos_ejemplo_entrada = {
        'ASI': 0.35,
        'attention_span_score': 5.8,
        # 'MHRI': 4.2,  <-- Añade aquí el resto de tus columnas reales
    }

# 1. Capturamos los datos dinámicamente por consola
    datos_usuario = solicitar_datos_usuario(FEATURES_OBLIGATORIAS)
    
    print("Procesando datos de ejemplo...")
    try:
        resultado = predecir_score_adiccion(datos_usuario)
        print(f"--> ¡Predicción completada con éxito!")
        print(f"--> El Addiction Score estimado para este registro es: {resultado:.2f}")
    except ValueError as err:
        print(f"Error en la predicción: {err}")
