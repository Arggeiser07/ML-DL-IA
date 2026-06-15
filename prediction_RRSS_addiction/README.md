# 📊 Sistema Predictivo de Adicciones

Aplicación interactiva web que utiliza un modelo matemático de **Regresión Lineal** para evaluar y predecir niveles de riesgo (como el uso de redes sociales o falta de atención) en tiempo real.

Hay dos versiones: una que se puede ejecutar en terminal , metiendo las variables que nos pide para hacer la prediccion a mano. Y otra que se puede ejecutar desde un navegador.

Se ha optado por la version interactiva web, ya que permite jugar con las variables con sliders y ver los resultados en tiempo real y resulta a nivel experimental mucho mas atractivo. A su vez se elimina la posibilidad de inputs no permitidos o caracteres que no sean numericos. 

No es una app con el fin de de llevar a cabo una investigacion exhaustiva, simplemente es para una practica end-to-end desde la toma de datos iniciales hasta su procesamiento y prediccion en un caso mas realista y en tiempo real.

El proyecto y el modelo son perfectamente adaptables a cualquier otro dataset o caso de prediccion real, ya que la estructura o el "molde" creado ( el pipeline ) son la finalidad de esta app.

---

## 🚀 Despliegue en 1 Clic

El proyecto está completamente contenedorizado con **Docker**. No necesitas instalar Python, Pandas, ni Scikit-Learn en tu máquina.

### Requisitos
* Tener abierto [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### Cómo ejecutar (Windows/Mac)
1. Descarga o clona la carpeta del proyecto.
2. Haz **doble clic** sobre el archivo `launch_app.bat` o 'launch_app.sh** si usas Linux/MacOs


*La aplicación se abrirá automáticamente en tu navegador en:* **http://localhost:8501**