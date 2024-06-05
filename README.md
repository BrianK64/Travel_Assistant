# Travel_Assistant
~~A travel assistant application leveraging a generative pre-trained transformer(GPT) model: a branch of large language models (LLMs).~~.\
An AI powered travel assistant application.

# Installation
Python 3.9.13\
requests 2.26.0\
beautifulsoup 4.12.3

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

   