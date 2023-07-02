import json
import os
import requests

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
REDIRECT_URI = "REDIRECT_URI"
TOKEN_URL = "https://allegro.pl.allegrosandbox.pl/auth/oauth/token"
USER_TOKEN = os.environ.get("USER_TOKEN")


class MyCustomException(Exception):
    pass


def get_access_token():
    try:
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(
            TOKEN_URL,
            data=data,
            verify=True,
            allow_redirects=True,
            auth=(CLIENT_ID, CLIENT_SECRET)
        )
        tokens = json.loads(access_token_response.text)
        return tokens['access_token']

    except requests.exceptions.RequestException as e:
        print("Error while getting access token:", e)
        return None
