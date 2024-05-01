# Travel_Assistant
A travel assistant application leveraging a branch of large language models (LLMs): a generative pre-trained transformer (GPT)

# To-Do List:
  1. Import OpenAI library.
  2. Get OpenAI (ChatGPT) API key(s)
  3. Create a model
  4. Feed the model with examples (Few-Shot Prompting)
  5. Apply a new prompt
  6. Receive a response

# Prompt Completion Structure
  ## Format
  In the process of training the model, examples that are provided to the model would be in this structured format:\
    {"Start_Date": <Start_Date_Placeholder>,\
    {"End_Date": <End_Date_Placeholder>,\
    "Location": <Location_Placeholder>,\
    "Count": <Number_of_People_Placeholder>,\
    "Theme": <Theme_Placeholder>,\
    "Accomodation#": <Accomodation#_Placeholder>,\
    "Acoomodation#_Duration: <Accomodation#_Duration_Placeholder>,\
    "Pet": <Pet_Placeholder>}\
    
  ## Explanation
  Here, a entry "Accomodation" has number count # attached to account for switching hotels, inns, etc.\

  Start_Date stands for date the travel starts.\
  End_date stands for date the travel ends.\
  Location stands for the location/area the use is staying\
  Count stands for the number of people the user is traveling with, including user themselves.\
  Theme stands for the main purpose of the trip, be it vacation, adventure, business, etc.\
  Accomodation stands for the place you are staying thoroughout the trip. Note users can have more than one accomodation during the entire travel duration.\
  Accomodation_Duration stands for the duration for which the user is staying at specific accomodation cite.\
  Pet stands for the presence of pet\
