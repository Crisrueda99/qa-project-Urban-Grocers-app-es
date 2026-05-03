# Proyecto QA - Urban Grocers (Sprint 8)

## Descripcion del proyecto

Este proyecto automatiza pruebas de API para la creacion de kits de productos en Urban Grocers.
El objetivo principal es validar el campo `name` en el endpoint de creacion de kits (`POST /api/v1/kits`) usando la lista de comprobacion del sprint.

Las pruebas incluyen escenarios positivos y negativos para verificar longitud, caracteres especiales, espacios, numeros, ausencia del parametro y tipo de dato incorrecto.

## Fuente de documentacion

- Documentacion del servidor Urban Grocers (apiDoc):
	`<URL_DEL_SERVIDOR>/docs/`
- Seccion usada para esta tarea: `Main.Kits -> Crear un kit`

## Tecnologias y tecnicas utilizadas

- Python 3
- pytest (framework de pruebas)
- requests (envio de solicitudes HTTP)
- Git y GitHub para control de versiones y entrega

Tecnicas aplicadas:

- Particion de pruebas en casos positivos y negativos
- Uso de funciones auxiliares para reutilizacion (`get_new_user_token`, `positive_assert`, `negative_assert_code_400`)
- Separacion de configuracion, datos de prueba, solicitudes y pruebas en archivos independientes

## Estructura del proyecto

- `configuration.py`: URL base y rutas de la API
- `data.py`: cuerpos de solicitud para usuario y kits
- `sender_stand_request.py`: funciones para enviar solicitudes POST
- `create_kit_name_kit_test.py`: pruebas automatizadas con pytest

## Como ejecutar las pruebas

1. Asegurate de tener Python instalado.
2. Crea y activa un entorno virtual (opcional pero recomendado).
3. Instala dependencias:
	 `pip install requests pytest`
4. Actualiza `configuration.py` con la URL actual del servidor lanzado en TripleTen.
5. Ejecuta las pruebas:
	 `pytest create_kit_name_kit_test.py -v`

## Notas

- Algunas pruebas negativas pueden aparecer como FAILED debido al comportamiento actual del backend; esto es esperado segun la lista de comprobacion del proyecto.