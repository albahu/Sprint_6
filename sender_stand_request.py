import configuration
import requests
import data
import json
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def get_token():
    response = post_new_user(data.user_body)
    response_data = response.json()
    return response_data['authToken']

def send_post_request(kit_body):
        auth_token = get_token()  # Con esto vas a jalar el token que has creado arriba
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT, headers=headers,
                                 json=kit_body)  # esta es la respuesta de la funcion, de tu api

        return response  # con esto retornamos la respuesta para usarla en una funcion



