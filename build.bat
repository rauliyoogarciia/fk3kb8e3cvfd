@echo off
REM Limpiar compilaciones anteriores
echo Limpiando carpetas de build y dist...
rd /s /q build
rd /s /q dist
del /f /q FiveChanger.spec

echo Limpiando caches de Python...
for /d /r . %%d in (__pycache__) do rd /s /q "%%d"

REM Instalar dependencias necesarias (ajusta si usas otro entorno)
echo Instalando dependencias...
pip install --upgrade pip
pip install --upgrade keyauth customtkinter

REM Crear ejecutable con PyInstaller
echo Compilando ejecutable con PyInstaller...
pyinstaller --onefile --add-data "utils;utils" --hidden-import=keyauth --hidden-import=utils.keyauth_manager main.py

echo Proceso finalizado.
pause
