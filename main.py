import json
import os

from authentication import get_access_token
from categories import get_main_categories, get_subcategory
from search import search_auctions


class AllegroAPI:
    def __init__(self):
        self.tokens = get_access_token()

    def main(self, parent_id):
        if self.tokens is None:
            print("Could not get access token.")
            return
        main_categories = get_main_categories()
        with open('Aktualne_Kategorie_Glowne.json', encoding='utf-8', mode='w') as f:
            json.dump(main_categories, f, indent=4, ensure_ascii=False)

        subcategories = {}
        for cat in main_categories['categories']:
            cat_id = cat['id']
            cat_name = cat['name']
            if cat_id == parent_id:
                subcategories[cat_name] = get_subcategory(parent_id)
        with open('Pod_Kategoria.json', encoding='utf-8', mode='w') as f:
            json.dump(subcategories, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    api = AllegroAPI()

    main_categories = get_main_categories()
    print("Dostępne główne kategorie:")
    for category in main_categories['categories']:
        print(category['id'], "-", category['name'])

    parent_id = input("Wybierz ID głównej kategorii: ")

    if not parent_id:
        print("ID kategorii nie może być puste.")
        exit()

    api.main(parent_id)

    search_phrase = "Szukana fraza przedmiotu"
    search_results = search_auctions(search_phrase)
    print(search_results)
