# IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

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

    # Setup webdriver
    # Create a new Selenium Service object which represents the WebDriver's connection to the browser's instance
    # This will automatically manage the ChromeDriver executable, which is needed by Selenium
    s = Service(ChromeDriverManager().install())

    # Create a Chrome WebDriver instance
    # Webdriver is a component of Selenium that interacts with the web browser
    driver = webdriver.Chrome(service=s)

    # Request the WebDriver to navigate to the URL.
    driver.get(url)

    # Wait for the dynamic content to load
    time.sleep(5)

    # Scroll down to the bottom of the page
    ## The JavaScript code "window.scrollTo(0, document.body.scrollHeight)" scrolls to the bottom of the
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the new content to load
    time.sleep(5)

    # Access page source (HTML)
    html = driver.page_source

    # Write the content of the HTML to a seprate text file.
    with open("assets/booking.html", 'w', encoding='utf-8') as file:
        file.write(html)

    # Close the browser
    driver.quit()

    return True


if __name__ == "__main__":
    main()