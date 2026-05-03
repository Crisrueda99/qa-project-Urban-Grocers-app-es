@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\Scripts\pytest.exe" (
  echo Error: no se encontro .venv\Scripts\pytest.exe
  echo Activa/crea el entorno virtual e instala pytest.
  exit /b 1
)

".venv\Scripts\pytest.exe" create_kit_name_kit_test.py -v > output.txt 2>&1

echo Pruebas finalizadas. Resultado guardado en output.txt
endlocal
