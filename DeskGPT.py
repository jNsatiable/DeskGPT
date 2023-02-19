def load_api_key():
    global api_key_input
    config.read('config.cfg')
    api_key_from_file = config['api_credentials']['api_key']

def get_api_key():
    global api_key_input
    try:
        print("API key not found.\n")
        time.sleep(1)
        api_key_input = input("Please input it here: ").strip()
        config['api_credentials'] = {}
        config['api_credentials']['api_key'] = api_key_input
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)    
        return api_key_input
    except Exception as ex:
        print(ex)


import openai, os, sys, time
import configparser
config = configparser.ConfigParser()

api_key_from_file = 0
while not api_key_from_file:
    try:
        load_api_key()
    except Exception as e:
        print(e)
        get_api_key()

#print(f'api_key_from_file: {api_key_from_file}')
print(f'api_key_input: {api_key_input}')

os.system('pause')

openai.api_key = api_key_from_file

def generate_response(prompt, max_tokens = 150):
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = max_tokens,
        n = 1,
        stop = None,
        temperature = 0.7)
    message = response.choices[0].text.strip()
    return message

print()
prompt = input("Enter prompt: ")
response = generate_response(prompt)

print(f'\nResponse: {response}\n')
