# Proyecto QA para Creación de Kits en Urban Grocers

Este proyecto automatiza pruebas para la API de creación de kits, enfocándose en la validación del campo 'name' según la lista de comprobación proporcionada.

## Cómo ejecutar las pruebas

1. Asegúrate de que Python y el entorno virtual estén configurados.

2. Instala las dependencias: pip install requests pytest

3. Actualiza `configuration.py` con la URL real del servidor obtenida después de lanzar el servidor.

4. Ejecuta las pruebas: pytest create_kit_name_kit_test.py

Las pruebas cubren escenarios positivos y negativos para el campo 'name' en las solicitudes de creación de kits.