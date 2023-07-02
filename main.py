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
        with open('Current_Main_Categories.json', encoding='utf-8', mode='w') as f:
            json.dump(main_categories, f, indent=4, ensure_ascii=False)

        subcategories = {}
        for cat in main_categories['categories']:
            cat_id = cat['id']
            cat_name = cat['name']
            if cat_id == parent_id:
                subcategories[cat_name] = get_subcategory(parent_id)
        with open('Sub_Category.json', encoding='utf-8', mode='w') as f:
            json.dump(subcategories, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    api = AllegroAPI()

    main_categories = get_main_categories()
    print("Main categories available:")
    for category in main_categories['categories']:
        print(category['id'], "-", category['name'])

    parent_id = input("Select main category ID: ")

    if not parent_id:
        print("Category ID cannot be empty.")
        exit()

    api.main(parent_id)

    search_phrase = "The search term for the item"
    search_results = search_auctions(search_phrase)
    print(search_results)
