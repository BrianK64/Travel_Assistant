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
    print("\nURL: "+url+"\n")

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the URL
        ## response.text is the raw HTML content of the web page fetched via requests
        ## 'html.parser' argument tells BeautifulSoup to use HTML parser to parse the document.
    soup = BeautifulSoup(response.text, "html.parser")

    return True


if __name__ == "__main__":
    main()