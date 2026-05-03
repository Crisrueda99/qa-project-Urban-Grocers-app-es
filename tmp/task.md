Proyecto para el Sprint 8: Tarea
Otro QA Engineer que trabaja contigo está comprobando cómo la aplicación Urban Grocers crea kits de productos. Se han creado varias listas de comprobación,
una de ellas es para el campo name en la solicitud de creación de un kit de productos.

Tu tarea es automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar el repositorio a revisión.

Configuración
Trabajarás con Git y GitHub en este proyecto. Sigue los pasos a continuación para configurar tu proyecto.

Paso 1: conecta tu GitHub
El primer paso es enlazar tu cuenta de GitHub a TripleTen. Para ello, haz clic en el botón "Enlazar la cuenta de GitHub" en el widget en la parte superior de esta página. Esto te llevará a una nueva pestaña del navegador donde se te pedirá que confirmes que deseas enlazar tu cuenta de GitHub. Si aún no has iniciado sesión en GitHub, se te pedirá que introduzcas tu nombre de usuario y contraseña. Al confirmarlo, tu perfil de TripleTen se conectará a tu perfil de GitHub a través de la API segura de GitHub. Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.

Paso 2. Clona el repositorio en tu computadora
Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Grocers-app-es.

Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

Abre la línea de comandos en tu computadora.
Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos. Por ejemplo:
cd ~               # asegúrate de estar en tu directorio de inicio
mkdir projects     # crea una carpeta llamada projects
cd projects        # cambia el directorio a la nueva carpeta de proyectos
Clona el repositorio con SSH.
git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git
💡 Asegúrate de clonar el repositorio correcto. El nombre de usuario debe ser tu propio nombre de usuario, no tripleten-com.

Paso 3. Trabaja con el proyecto de forma local
Ahora tienes una copia local del proyecto y puedes abrir la carpeta del proyecto en tu computadora.

💡 Puedes utilizar PyCharm para trabajar en el proyecto localmente. Simplemente abre PyCharm y selecciona Archivo → Abrir y luego selecciona la carpeta qa-project-Urban-Grocers-app-es que clonaste en tu computadora.

Cuando puedas comenzar a trabajar, presiona el botón "Iniciar el servidor" para obtener la URL de tu servidor.

Servidor
¡Genial, tu servidor ha sido iniciado!

Dirección del banco: https://cnt-df0fb0bc-8dd6-4563-8000-66ad11a6a848.containerhub.tripleten-services.com

 Documentación de la API: https://cnt-df0fb0bc-8dd6-4563-8000-66ad11a6a848.containerhub.tripleten-services.com/docs/

Aprende sobre el trabajo de un servidor en esta guía especial.


Reiniciar el servidor
Abre la documentación para estudiar la API de la aplicación de Urban Grocers: <the url of the launched server>/docs/.

Busca "Main.Kits" →" Crear un kit.”

Antes de comenzar a trabajar tu proyecto, lee cuidadosamente esta lección.



Creación de un kit para el usuario o usuaria
Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:

Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.
Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, según el cuerpo de solicitud. Sin embargo, los pasos serán los mismos.

Lista de comprobación de pruebas

№	Description	ER:
1	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
3	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
4	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
5	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
6	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400

Valores de prueba para las pruebas 2 y 4

El número permitido de caracteres (511):

kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

El número de caracteres es mayor que la cantidad permitida (512):

kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

Importante
Algunas pruebas devolverán FAILED como resultado; no te preocupes, es un comportamiento esperado dentro de la lista de comprobaciones.

Al enviar la solución, no olvides agregar los siguientes archivos: .gitignore y README.md. Agrega una breve descripción de tu proyecto. En el archivo README.md escribe las reglas o pasos para ejecutar las pruebas.

Necesitarás seis archivos en total: configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py, README.md, y .gitignore. Puedes nombrarlos de otra forma, sin embargo, estos nombres describen con precisión el contenido de estos archivos, por lo que son buenas opciones de nombres. Consulta las pistas a continuación para más detalles.

Pistas

URL y rutas de solicitud

Es mejor almacenar todas las rutas en el archivo configuration.py.

Envío de las solicitudes.

Todas las solicitudes que necesitas para resolver la tarea se pueden almacenar en el archivo sender_stand_request.py.
Copia la solicitud para crear un nuevo usuario o usuaria de la lección sobre solicitudes POST.
La función para crear un nuevo kit de producto puede denominarse post_new_client_kit
Utiliza dos parámetros en la función para crear un nuevo kit de producto: kit_body (el cuerpo de solicitud) y auth_token (el token de autenticación).
Si utilizas el diccionario de datos del archivo data.py una vez más, aplícale la función copy(). Es mejor no hacer ningún cambio en el diccionario de origen, ya que esto puede generar errores.
Si la solicitud se envía con un error, comprueba las barras (//), especialmente las del final.

Datos.

Coloca los cuerpos de la solicitud POST en el archivo data.py.

Pruebas

La lista de comprobación completa debe estar en el archivo create_kit_name_kit_test.py.
Lo ideal es que especifiques los archivos y directorios para iniciar Pytest. De lo contrario, Pytest buscará las pruebas en el directorio y los subdirectorios de trabajo actuales. Necesita los archivos que comienzan con test_ o terminan con _test. La búsqueda no distingue entre mayúsculas y minúsculas, por lo que puede encontrar tanto Test_1.py como test_1.py.
Puedes crear una función que cambiará el contenido del cuerpo de solicitud, nómbrala get_kit_body y agrega el parámetro name.
Hay dos tipos de pruebas en la lista de comprobación: positivas y negativas (código 400). Su lógica se puede expresar en funciones separadas: positive_assert(kit_body) y negative_assert_code_400(kit_body):.
Recibir el token también puede ser una función separada. Llámala get_new_user_token().
Cada prueba debe estar en una función separada con el prefijo test, de lo contrario, Pytest las ignorará.

El archivo README.md

Utiliza https://dillinger.io/ para comprobar lo que has escrito.
Reutiliza el archivo README.md de la lección "Archivos de proyecto auxiliares: gitignore y README".

El archivo .gitignore

Reutiliza el archivo .gitignore de la lección "Archivos de proyecto auxiliares: gitignore y README".
Entrega de tu proyecto
Cuando quieras enviar tus pruebas para su revisión, inicia el servidor de Urban Grocers de nuevo para obtener una nueva URL. Utilízala para actualizar la URL en el archivo configuration.py. Este paso es necesario para garantizar que GitHub funcione bien con nuestro servidor.

Confirma y envía, o empuja, tus cambios.

El proyecto se evaluará de acuerdo con esta lista de comprobación. Si no se acepta tu proyecto en el primer intento, tienes 48 horas para volver a enviarlo.

Las revisiones tardan hasta 48 horas y recibirás todo tu feedback por medio de la plataforma. Después de enviar el proyecto, te recomendamos que revises regularmente la plataforma (una vez al día) para confirmar si tienes feedback.

Si tienes alguna pregunta, no dudes en hacerla en Discord. 

💡 Recuerda, tu código debe verse ordenado y no debe contener variables no utilizadas.
