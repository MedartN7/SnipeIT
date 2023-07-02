import os
import base64
import hashlib
import secrets
import string
import requests
import json
from cachetools import TTLCache 

CLIENT_ID = "CLIENT_ID"          # enter the Client_ID of the application
CLIENT_SECRET = "CLIENT_SECRET"      # enter the application's Client_Secret
REDIRECT_URI = "REDIRECT_URI"       # enter redirect_uri
AUTH_URL = "https://allegro.pl.allegrosandbox.pl/auth/oauth/authorize"
TOKEN_URL = "https://allegro.pl.allegrosandbox.pl/auth/oauth/token"

token_cache = TTLCache(maxsize=1, ttl=10)  # Cache for token, validity 10 seconds.


def generate_code_verifier():
    code_verifier = ''.join((secrets.choice(string.ascii_letters) for i in range(40)))
    return code_verifier


def generate_code_challenge(code_verifier):
    hashed = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    base64_encoded = base64.urlsafe_b64encode(hashed).decode('utf-8')
    code_challenge = base64_encoded.replace('=', '')
    return code_challenge


def get_authorization_code(code_verifier):
    code_challenge = generate_code_challenge(code_verifier)
    authorization_redirect_url = f"{AUTH_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}" \
                                 f"&code_challenge_method=S256&code_challenge={code_challenge}"
    print("Log in to Allegro - use the url in your browser and enter the authorization code from the returned url: ")
    print(f"--- {authorization_redirect_url} ---")
    authorization_code = input('code: ')
    return authorization_code


def get_access_token(authorization_code, code_verifier):
    try:
        data = {'grant_type': 'authorization_code', 'code': authorization_code,
                'redirect_uri': REDIRECT_URI, 'code_verifier': code_verifier
    }
        access_token_response = requests.post(TOKEN_URL, data=data, verify=True, allow_redirects=False)
        response_body = json.loads(access_token_response.text)
        return response_body['access_token']

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def get_cached_access_token():
    if 'access_token' in token_cache:
        return token_cache['access_token']
    else:
        code_verifier = generate_code_verifier()
        authorization_code = get_authorization_code(code_verifier)
        access_token = get_access_token(authorization_code, code_verifier)
        token_cache['access_token'] = access_token
    return access_token

def main():
    access_token = get_cached_access_token()
    os.environ["USER_TOKEN"] = access_token 

if __name__ == "__main__":
    main()