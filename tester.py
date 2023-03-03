
import configparser
config = configparser.ConfigParser()


config.read('config.cfg')
api_key_from_file = config['api_credentials']['api_key']
engine = config['params']['engine']
max_tokens = config['params']['max_tokens']
n = config['params']['n']
temperature = config['params']['temperature']


api_key_input = input("Paste your API Key here then press Enter: ").strip()
# -- default values -- #
config['params'] = {}
config['params']['engine'] = "text-davinci-003"
config['params']['max_tokens'] = "200"
config['params']['n'] = "1"
config['params']['temperature'] = "0.7"
# ---------------------#        

config['api_credentials'] = {}
config['api_credentials']['api_key'] = str(api_key_input)
with open('config.cfg', 'w') as configfile:
    config.write(configfile)