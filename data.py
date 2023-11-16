import configuration
from configuration import URL_SERVICE
import requests

url = f"{configuration.URL_SERVICE}/api/v1/users/"


json_data = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
headers = {
    "Content-Type": "application/json"
}


response = requests.post(url, json=json_data, headers=headers)


if response.status_code == 201:
    print("Solicitud POST exitosa. Datos enviados correctamente.")
    print("Respuesta del servidor:", response.json())
else:
    print(f"Error al enviar la solicitud. Código de respuesta: {response.status_code}")
    print("Mensaje de error:", response.text)

def get_kit_body():
    return None


def send_post_request():
    return None
