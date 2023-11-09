import requests


url = "https://63a5fab1-215b-4b49-bf84-da3e7d9f1c70.serverhub.tripleten-services.com/api/v1/users/"
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
