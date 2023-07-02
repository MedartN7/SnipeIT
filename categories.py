import json
import requests
import requests.exceptions

from authentication import get_access_token

TOKEN_URL = "https://allegro.pl.allegrosandbox.pl/auth/oauth/token"
SALE_CATEGORIES_URL = "https://api.allegro.pl.allegrosandbox.pl/sale/categories"

class MyCustomException(Exception):
    pass

def get_main_categories():
    try:
        headers = {'Authorization': 'Bearer ' + get_access_token(), 'Accept': "application/vnd.allegro.public.v1+json"}
        params = {'fallback': False, 'limit': 50, 'searchMode': 'DESCRIPTIONS'}
        main_categories_result = requests.get(
            SALE_CATEGORIES_URL,
            headers=headers,
            verify=True,
            params=params,
            allow_redirects=True
        )
        return main_categories_result.json()

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_subcategory(parent_id):
    try:
        url = f"https://api.allegro.pl.allegrosandbox.pl/sale/categories/{parent_id}/children"
        headers = {'Authorization': 'Bearer ' + get_access_token(), 'Accept': "application/vnd.allegro.public.v1+json"}
        subcategory_result = requests.get(url, headers=headers, verify=True, allow_redirects=True)
        subcategory = subcategory_result.json()
        return subcategory

    except requests.exceptions.HTTPError as err:
        print("HTTP Error while getting subcategory:", err)
        raise MyCustomException("Error while getting subcategory: HTTP Error") from err
