```bash
#!/bin/bash
echo "Verificando Docker..."
if ! docker info >/dev/null 2>&1; then
    echo "ERROR: Docker no está arrancado. Por favor, abre Docker Desktop."
    exit 1
fi
echo "Limpiando contenedores antiguos..."
docker compose down
echo "Abriendo el navegador..."
python3 -m webbrowser http://localhost:8501 || open http://localhost:8501 || xdg-open http://localhost:8501
echo "Levantando la aplicación..."
docker compose up --build