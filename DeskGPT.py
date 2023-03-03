def load_api_key():
    """
    Function to load the API key from a file
    """
    global api_key_from_file, engine, max_tokens, n, temperature
    config.read('resources/config.cfg')
    api_key_from_file = config['api_credentials']['api_key']
    engine = config['params']['engine']
    max_tokens = config['params']['max_tokens']
    n = config['params']['n']
    temperature = config['params']['temperature']
    if api_key_from_file == '':
        print("There is a problem with your API Key.\n")
        get_api_key()
        load_api_key()
    else:
        pass

def get_api_key():
    """
    Function to get the API key from user input and save it to a file
    """
    try:
        time.sleep(1)
        api_key_input = input("Paste your API Key here then press Enter: ").strip()
        print()

        # -- default values -- #
        config['params'] = {}
        config['params']['engine'] = "text-davinci-003"
        config['params']['max_tokens'] = "200"
        config['params']['n'] = "1"
        config['params']['temperature'] = "0.7"
        # ---------------------#        

        config['api_credentials'] = {}
        config['api_credentials']['api_key'] = str(api_key_input)
        with open('resources/config.cfg', 'w') as configfile:
            config.write(configfile)
        api_key_from_file = api_key_input
        time.sleep(2)
    except Exception as e:
        print(e)

def test_response():
    """
    Function to confirm if API Key works
    """
    try:
        openai.api_key = api_key_from_file
        test_response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = ""
        )
    except Exception as e:
        print(e)
        config['api_credentials']['api_key'] = ""   # -- clear API key entry
        with open('resources/config.cfg', 'w') as configfile: # -- update config file
            config.write(configfile)
        #os.remove('resources/config.cfg') # -- delete config file if API Key is problematic (expired, invalid, etc.)
        input('Press any key to exit...')
        sys.exit()

def generate_response(prompt):
    """
    Function specifying the parameters of the response as well as
    actually returning it.
    """
    response = openai.Completion.create(
        engine = "text-davinci-003",    # -- the model to use
        prompt = prompt,
        max_tokens = 200,   # -- the maximum 'words' in prompt + 'words' in response
        n = 1,  # -- the number or responses
        stop = None,    # -- specifies a stop sequecn e.g. a new line char
        temperature = 0.7)
    message = response.choices[0].text.strip()
    return message

import os, sys, openai, time, configparser
config = configparser.ConfigParser()

api_key_from_file = 0
while not api_key_from_file:
    try:
        load_api_key()
        test_response()
    except Exception as e:
        print("There is a problem with your API Key.\n")
        get_api_key()

openai.api_key = api_key_from_file

print(f'SETTINGS: engine = {engine}, max_tokens = {max_tokens}, n = {n}, temperature = {temperature}\n')

prompt = 0  # -- initialize value of prompt
while True: # -- start a loop
    prompt = input("Enter prompt: ")    # -- ask user for input
    if prompt != '':    # -- when input is not blank: generate response
        response = generate_response(prompt)
        print(f'\nDeskGPT: \n{response}\n')    
    else:   # -- when input is blank: quit app
        print('No prompt provided. Exiting program...')
        time.sleep(1)
        break

