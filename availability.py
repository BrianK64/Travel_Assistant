# IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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

    # Access the page source (HTML)
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content and store it in a BeautifulSoup variable.
    soup = BeautifulSoup(html, "html.parser")
        
    # Get each hotel's property card contents from HTML, which is stored in a BeautifulSoup variable "soup"
    # each hotel property card container has attribute data-testid = 'property-card-container'
    for container in soup.find_all('div', {'data-testid': 'property-card-container'}):

        # Error handling for HTML elements with missing/inconsistent attribute values - title
        try:
            title = container.find('div', {'data-testid': 'title'}).text
        except AttributeError:
            title = None

        # Error handling for HTML elements with missing/inconsistent attribute values - location
        try:
            location = container.find('span', {'data-testid':'address'}).text
        except AttributeError:
            location = None

        proximity = container.find('span', {'data-testid': 'distance'}).text
        rating = container.find('div', {'data-testid': 'review-score'}).text[0:3]
        # an external link to a table of available unit list
        availability_url = container.find('a', {'data-testid': 'availability-cta-btn'})['href']
        #room_configurations    <span class="a21c5c4883">
        #beds   <div class="abf093bdfe">

        if (title == "The Rittenhouse Hotel" and location == "Center City, Philadelphia") or (title == "Philadelphia Airport Marriott" and location == "Philadelphia"):
            pass
        else:
            print("-"*100)
            print(f"Hotel: {str(title)}\tLocation: {str(location)}\tProximity: {proximity}\tRating: {rating}\n")
            
            inner_s = Service(ChromeDriverManager().install())
            inner_driver = webdriver.Chrome(service=inner_s)
            inner_driver.get(availability_url)
            time.sleep(5)
            inner_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            inner_html = inner_driver.page_source
            inner_driver.quit()
            
            inner_soup = BeautifulSoup(inner_html, 'html.parser')
            table = inner_soup.find('table', {'id': 'hprt-table'})

            last_seen_apartment_type = None
            for unit in table.select('tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-last-row, tr.js-rt-block-row.e2e-hprt-table-row'):  #table.find_all('tr', {'class': 'js-rt-block-row e2e-hprt-table-row hprt-table-last-row'}):
                classes = unit.get('class', [])
                
                if unit.find('a', {'class': 'hprt-roomtype-link'}) is None:
                    room = last_seen_apartment_type
                else:
                    room = unit.find('a', {'class': 'hprt-roomtype-link'}).text
                    last_seen_apartment_type = room
                
                # Get price
                room_price = unit.find('span', {'class': 'prco-valign-middle-helper'}).text

                """
                if 'hprt-table-last-row' not in classes:
                    print("---multiple choices---\n")
                    if unit.find('a', {'class': 'hprt-roomtype-link'}) is not None:
                        room = unit.find('a', {'class': 'hprt-roomtype-link'})
                        last_seen_apartment_type = room
                    else:
                        room = last_seen_apartment_type

                else:
                    print('---single choice---\n')
                    room = unit.find('a', {'class': 'hprt-roomtype-link'})
                """

                # Cleaning white empty lines
                #room = '\n'.join([line for line in room.split('\n')])
                #room_price = '\n'.join([line for line in room_price.split('\n')])
                room = room.strip()
                room_price = room_price.strip()

                print(f"{room}: \t{room_price}")

    return True


if __name__ == "__main__":
    main()

"""
# URL to the hotel's external link to a table listing available units
url = "https://www.booking.com/hotel/us/mint-house-philadelphia-divine-lorraine.html?aid=304142&label=gen173nr-1FCAQoggJCE3NlYXJjaF9waGlsYWRlbHBoaWFIMVgEaH2IAQGYATG4ARfIAQzYAQHoAQH4AQOIAgGoAgO4Aqm1tbMGwAIB0gIkYjY0ZDQ1YmYtOWE4Yy00NTIzLTk4NzAtNTY3YWFmMzJmZWY42AIF4AIB&sid=535d37135c3a8eecf886dd78f0dfb87d&all_sr_blocks=897035008_394176834_4_0_0;checkin=2024-06-22;checkout=2024-06-23;dist=0;group_adults=3;group_children=0;hapos=1;highlighted_blocks=897035008_394176834_4_0_0;hpos=1;matching_block_id=897035008_394176834_4_0_0;no_rooms=2;req_adults=3;req_children=0;room1=A;room2=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=897035008_394176834_4_0_0__25439;srepoch=1718442677;srpvid=68a6409469500064;type=total;ucfs=1&"

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

# Access the page source (HTML)
html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content and store it in a BeautifulSoup variable.
soup = BeautifulSoup(html, "html.parser")

table = soup.find('table', {'id': 'hprt-table'})

with open("assets/availableunits.html", 'w', encoding='utf-8') as file:
    for unit in table.find_all('tr', {'class': 'js-rt-block-row e2e-hprt-table-row hprt-table-last-row'}):
        file.write(str(unit)+'\n' + '-'*150)
        for room in unit.find_all('li', {'class': 'bedroom_bed_type'}):
            print(room.text)
"""