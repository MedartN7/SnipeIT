# SnipeIT

Script for interacting with the Allegro API. Incomplete and suspended until full access to their API is obtained or i'll try another way:).
Read more at:
1. [Allegro API Access Restrictions Announcement](https://allegro.pl/dla-sprzedajacych/1-czerwca-2021-w-api-allegro-ograniczymy-dostep-do-publicznych-danych-o-sprzedazy-innych-uzytkownikow-i-zmienimy-forme-ich-udostepniania-O3BlgZVdwCa)
2. [Allegro API GitHub Issue](https://github.com/allegro/allegro-api/issues/4221)

Description
The goal of the application was to enable the use of the Allegro API for retrieving information about product categories and searching for auctions on Allegro, bidding, etc.
Work on the project has been suspended, but I will come back to it someday. I leave it where I left off for those interested in similar tools.

Requirements
Python 3.6+
Libraries: requests and cachetools

Installation

1. Clone the repository:

2. Navigate to the project directory:
```
cd AllegroAPI
```

3. Install dependencies:
```
pip install requests
pip install cachetools
```

4. Configure environment variables:

- Create a .env file in the project directory.

- Add the following environment variables:
```
CLIENT_ID="Your_Client_ID"
CLIENT_SECRET="Your_Client_Secret"
REDIRECT_URI="Your_Redirect_URI"
USER_TOKEN="Your_User_Token"
```


Code Structure
- `authentication.py`: Module containing a function for obtaining access token from the Allegro API.
- `categories.py`: Module containing functions for retrieving product categories from the Allegro API.
- `search.py`: Module containing a function for searching auctions on the Allegro API.
- `main.py`: Main script that utilizes functions from the other modules.

Author
Bartłomiej Walecki
