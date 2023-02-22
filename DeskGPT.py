"""
Version 0.1.00
"""

def load_api_key():
    """
    Function to load the API key from a file
    """
    global api_key_from_file
    config.read('config.cfg')
    api_key_from_file = config['api_credentials']['api_key']

def get_api_key():
    """
    Function to get the API key from user input and save it to a file
    """
    try:
        print("API key not found.\n")
        time.sleep(1)
        api_key_input = input("Please input it here: ").strip()
        config['api_credentials'] = {}
        config['api_credentials']['api_key'] = str(api_key_input)
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)    
    except Exception as ex:
        print(ex)

def generate_response(prompt, max_tokens = 1000):
    """
    Function specifying the parameters of the response as well as
    actually displaying it.
    """
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = max_tokens,
        n = 1,
        stop = None,
        temperature = 0.9)
    message = response.choices[0].text.strip()
    return message

import openai, time
import configparser
config = configparser.ConfigParser()

api_key_from_file = 0
while not api_key_from_file:
    try:
        load_api_key()
    except Exception as e:
        print(e)
        get_api_key()

openai.api_key = api_key_from_file

prompt = 0  # -- initialize value of prompt
while True: # -- start a loop that repeats until a break / return is called
    prompt = input("Enter prompt: ")    # -- ask for input
    if prompt != '':    # -- when input is not blank
        response = generate_response(prompt)
        print(f'\nResponse: {response}\n')    
    else:   # -- when input is blank
        print('No prompt provided. Exiting program.')
        time.sleep(1)
        break

