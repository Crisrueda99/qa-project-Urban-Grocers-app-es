import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, CREATE_KIT_PATH
from data import user_body

def post_new_user(user_body):
    response = requests.post(URL_SERVICE + CREATE_USER_PATH, json=user_body)
    return response

def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": "Bearer " + auth_token}
    response = requests.post(URL_SERVICE + CREATE_KIT_PATH, json=kit_body, headers=headers)
    return response

def get_new_user_token():
    response = post_new_user(user_body)
    if response.status_code == 201:
        return response.json()["authToken"]
    else:
        print(f"Failed to create user: {response.status_code} {response.text}")
        raise Exception("Failed to create user")