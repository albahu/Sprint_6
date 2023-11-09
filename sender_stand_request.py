
import requests
URL_SERVICE = "https://63a5fab1-215b-4b49-bf84-da3e7d9f1c70.serverhub.tripleten-services.com/api/v1/users"
def send_post_request(kit_body):
    url = f"{URL_SERVICE}/api/v1/kits"
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=kit_body, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

# Pruebas de envío de solicitudes según la lista de comprobación
def test_requests():
    kit_body_1 = {"name": "a"}
    kit_body_2 = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    kit_body_3 = {"name": ""}
    kit_body_4 = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    kit_body_5 = {"name": "*%@"}
    kit_body_6 = {"name": " A Aaa "}
    kit_body_7 = {"name": "123"}
    kit_body_8 = {}
    kit_body_9 = {"name": 123}

if __name__ == '__main__':
    test_requests()



