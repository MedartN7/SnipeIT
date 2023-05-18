import json
import requests

from authentication import get_access_token

OFFERS_LISTING_URL = "https://api.allegro.pl.allegrosandbox.pl/sale/products"


def search_auctions(search_phrase):
    headers = {
        "Authorization": 'Bearer ' + get_access_token(),
        'Accept': "application/vnd.allegro.public.v1+json",
        "Accept-Language": "PL",
        "Content-Type": "application/json",
    }
    params = {
        "category.id": "category.id", 
        "phrase": search_phrase,
        "searchMode": "DESCRIPTIONS",
        "offset": 550,
        "limit": 50,
        "sort": "-startTime",
    }
    response_result = requests.get(
        OFFERS_LISTING_URL,
        headers=headers,
        params=params,
        verify=True,
        allow_redirects=True
    )
    response = response_result.json()
    return response
