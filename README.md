# Travel_Assistant
~~A travel assistant application leveraging a generative pre-trained transformer(GPT) model: a branch of large language models (LLMs).~~.\
An AI powered travel assistant application.

# Installation
Python 3.9.13\
requests 2.26.0\
beautifulsoup 4.12.3\
selenium 4.21.0

# To-Do List:
  1. Data Collection and Validation
  2. Accomodation Management
  3. AI Recommendation System
  4. User Interface
  5. Test
  6. Deploy

# Data Management
  ## Format
  In the process of training the model, examples that are provided to the model would be in this structured format:\
    {"Start_Date": <Start_Date_Placeholder>,\
    "End_Date": <End_Date_Placeholder>,\
    "Location": <Location_Placeholder>,\
    "Count": <Number_of_People_Placeholder>,\
    "Theme": <Theme_Placeholder>,\
    "Accomodation#": <Accomodation#_Placeholder>,\
    "Acoomodation#_Duration: <Accomodation#_Duration_Placeholder>,\
    "Pet": <Pet_Placeholder>}

  ## Datatypes
  {"Start_Date": datetime,\
    "End_Date": datetime,\
    "Location": string,\
    "Count": integer,\
    "Theme": string,\
    "Accomodation#": string,\
    "Acoomodation#_Duration: tuple,\
    "Pet": boolean}
    
  ## Description
  Here, the entry "Accomodation" has number count # attached to account for switching hotels, inns, etc.\
  *Start_Date* stands for date the travel starts.\
  *End_date* stands for date the travel ends.\
  *Location* stands for the location/area the use is staying\
  *Count* stands for the number of people the user is traveling with, including user themselves.\
  *Theme* stands for the main purpose of the trip, be it vacation, adventure, business, etc.\
  *Accomodation* stands for the place you are staying thoroughout the trip. Note users can have more than one accomodation during the entire travel duration.\
  *Accomodation_Duration* stands for the duration for which the user is staying at specific accomodation cite.\
  *Pet* stands for the presence of pet.

  ## Validation
  *Start_date* should come before **End_date*.\
  *Accomodation#* should fall within the entire duration of travel.\
  *Count* filed should be a positive integer.\
  *Theme* should be one of the predefined definitions

# Resources
https://www.scrapingbee.com/blog/web-scraping-booking/  \
https://www.booking.com/

# Encountered Challenges
## Issue 1 - 06/10/2024
The original code in this project was designed to scrape hotel data - names, locations, ratings, ammenties, etc. from one of the most commonly used hotel booking websites, Booking.com, using Python and packages `request` and `beautifulSoup`. However, it has been observed that the code does not work as intended after succesfully creating a BeautifulSoup object for parsing the html data. The main problem lies in the fact that the specific elements of html the code tries to find and extract are not present in the response content when GET request has been sent to the URL.
### Resolution
To overcome this issue, a new Python code has been created along with local asset files. This new Python code simulates what the original code was supposed to do by using local HTML file which must be manually saved by users from the URL generated by the original code. This local HTML file ensures that the required elements are present and can be accessed consistently.
### Fix - 06/13/2024
Use `selenium` driver instead of `BeautifulSoup` to extract HTML content from Booking.com website. Booking.com uses JavaScript to load content dynamically, meaning the website loads small chunk at a time when user scrolls down to the bottom of the page. selenium enables automation of real web browser by executing JavaScript code, allowing the interaction with dynamic webpage content. In this code, the browser selenium uses to automate web browser is Chrome. Pausing the program by executing the function _time.sleep()_ is crucial to allow dynamic content to fully load.