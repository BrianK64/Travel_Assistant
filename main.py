# IMPORTS
import requests
from bs4 import BeautifulSoup

lang = {
    "English": "en-us",
    "Korean": "ko"
}

def main():

    # User's preferred language
    completed = 0
    while not completed:
        lang_id = input("Select your language: ")
        if lang_id in lang:
            lang_id = lang[lang_id]
            completed = 1
        else:
            print("Selected language not supported\n")

    # Get the destination from user
    city_id = input("Where are you going? ")

    # Get the url
    url = f"https://www.booking.com/searchresults.html?ss={city_id}&lang={lang_id}"

    return url

if __name__ == "__main__":
    print(main())