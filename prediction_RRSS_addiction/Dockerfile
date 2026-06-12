# 1. Usamos una imagen oficial de Python ligera como base
FROM python:3.10-slim

# 2. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de requisitos primero (para optimizar la caché de Docker)
COPY requirements.txt .

# 4. Instalamos las librerías de Python sin guardar temporales
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo el código de nuestro proyecto al contenedor
# (Esto incluirá tu main.py y la carpeta src/ con el modelo .pkl)
COPY . .

# 6. Comando por defecto para arrancar la aplicación
CMD ["python", "src/main.py"]