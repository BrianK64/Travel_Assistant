# IMPORTS
import requests
from bs4 import BeautifulSoup

# Mapping languages to their corresponding codes
lang = {
    "English": "en-us",
    "Korean": "ko"
}

def main():

    ### Get users' preferred language ###
    completed = 0
    # Language Selection Loop
    while not completed:
        lang_id = input("Select your language: ")
        # Check if the selected language is supported
        if lang_id in lang:
            # get the corresponding language code
            lang_id = lang[lang_id]
            completed = 1
        else:
            print("Selected language not supported\n")

    # Get users' destination
    city_id = input("Where are you going? ")

    # Get check-in and check-out dates
    # Datetime must be in FFG (YYYY-MM-DD) format
    checkin = input("State Date: (YYYY-MM-DD) ")
    checkout = input("End Date: (YYYY-MM-DD) ")

    # Get details for booking hotels
    group_adults = input("How many adults? ")
    group_children = input("How many children? ")
    no_rooms = input("How many rooms? ")

    # Construct the URL for the search results page on booking.com with user-provided information.
    url = f"https://www.booking.com/searchresults.html?ss={city_id}&lang={lang_id}&checkin={checkin}&checkout={checkout}&group_adults={group_adults}&no_rooms={no_rooms}&group_children={group_children}"
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