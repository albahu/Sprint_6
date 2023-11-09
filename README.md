# Proyecto 6
# Kit de Usuario o Usuaria - Pruebas de API

Este proyecto consiste en la creación de un kit para un usuario o usuaria particular utilizando solicitudes API. A continuación se detallan los pasos para ejecutar las pruebas correctamente.

## Instrucciones para Ejecutar las Pruebas

1. **Configuración del Entorno:**
   - Asegúrate de tener Python instalado en tu sistema.
   - Clona este repositorio en tu máquina local.

2. **Instalación de Dependencias:**
   - Ejecuta `pip install -r requirements.txt` para instalar las dependencias necesarias.

3. **Configuración de Variables de Entorno:**
   - Crea un archivo llamado `config.env` y agrega el token de autenticación en la siguiente forma:
     ```
     AUTH_TOKEN=YOUR_AUTH_TOKEN_HERE
     ```

4. **Ejecución de las Pruebas:**
   - Ejecuta el siguiente comando en tu terminal:
     ```
     pytest
     ```

5. **Ver Resultados:**
   - Revisa la consola para ver el resultado de las pruebas. Asegúrate de verificar si alguna prueba devuelve 'FAILED', lo cual puede ser un comportamiento esperado en ciertos casos.

## Archivos y Estructura del Proyecto

- `configuration.py`: Contiene las rutas y URL de las solicitudes API.
- `data.py`: Almacena los cuerpos de solicitud POST.
- `sender_stand_request.py`: Contiene las funciones para enviar solicitudes API.
- `create_kit_name_kit_test.py`: Lista de comprobación de pruebas en forma de funciones de prueba.
- `README.md`: Este archivo, proporciona instrucciones para ejecutar las pruebas.
- `.gitignore`: Archivo que especifica los archivos y directorios que Git debe ignorar.

## Notas Importantes

- Algunas pruebas pueden devolver 'FAILED' como resultado, lo cual es un comportamiento esperado dentro de la lista de comprobaciones.
- Asegúrate de seguir los pasos proporcionados y verificar que los resultados de las pruebas coincidan con las expectativas.
