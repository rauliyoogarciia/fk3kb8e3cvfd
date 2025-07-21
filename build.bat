@echo off
setlocal enabledelayedexpansion

echo Preparando entorno...
pause

echo Instalando customtkinter...
"C:\Users\Rauhh\AppData\Local\Programs\Python\Python310\python.exe" -m pip install customtkinter
pause

echo Limpiando compilaciones anteriores...
rd /s /q build
rd /s /q dist
del /f /q main.spec
pause

echo Compilando con PyInstaller...
"C:\Users\Rauhh\AppData\Local\Programs\Python\Python310\python.exe" -m PyInstaller --onefile --noconsole main.py
if errorlevel 1 (
    echo Hubo un error durante la compilacion.
    pause
    exit /b 1
)

echo Compilacion finalizada. El .exe esta en la carpeta dist.
pause

:: Define rutas Tcl y Tk
set TCL_PATH=C:\Users\Rauhh\AppData\Local\Programs\Python\Python310\tcl\tcl8.6
set TK_PATH=C:\Users\Rauhh\AppData\Local\Programs\Python\Python310\tcl\tk8.6

:: Verificar si las rutas existen y mostrar mensaje
if exist "!TCL_PATH!" (
    echo Ruta Tcl encontrada: !TCL_PATH!
) else (
    echo Ruta Tcl NO encontrada: !TCL_PATH!
)

if exist "!TK_PATH!" (
    echo Ruta Tk encontrada: !TK_PATH!
) else (
    echo Ruta Tk NO encontrada: !TK_PATH!
)

pause
