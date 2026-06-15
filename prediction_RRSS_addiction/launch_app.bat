@echo off
title Lanzador de Aplicación Predictiva - Streamlit + Docker
cls

echo =========================================================
echo    INICIANDO EL SISTEMA PREDICTIVE DE ADICCIONES
echo =========================================================
echo.

:: 1. Comprobamos si Docker Desktop está corriendo
echo [1/3] Verificando el motor de Docker...
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Docker Desktop no está arrancado o se está iniciando.
    echo Por favor, abre Docker Desktop y vuelve a ejecutar este archivo.
    echo.
    pause
    exit
)

:: 2. Apagamos posibles residuos zombis del contenedor
echo [2/3] Limpiando contenedores antiguos en segundo plano...
docker compose down >nul 2>&1

:: 3. Abrimos el navegador automáticamente en segundo plano
echo [3/3] Levantando entorno gráfico interactivo...
echo.
echo Abriendo http://localhost:8501 en tu navegador...
start "" "http://localhost:8501"
echo.
echo ---------------------------------------------------------
echo LOGS DEL CONTENEDOR (Presiona Ctrl+C aquí para detener):
echo ---------------------------------------------------------

docker compose up --build

pause