# Imports
from openai import OpenAI
import os
from dotenv import load_dotenv

def main():

    try:
        # Get configuration settings
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("OPENAI_MODEL")

        # Initialize the OpenAI client
        client = OpenAI(
            api_key=api_key
        )

        # Establish a system message
        system_message = "I am a travel assistant who helps users discover and plan their future trips."

        # Get user prompt
        user_input = input("\nMessage ChatGPT\n")

        # Initialize an array or messages
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "context": user_input}
        ]

        # Send request to OpenAI client
        response = client.chat.completions.create(
            model = model,
            messages = messages
        )

        print(generated_text = response.choices[0].message)



    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()