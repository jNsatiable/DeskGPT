
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'var1': '1', 'var2': 'yes'}
config['user.deets'] = {'username': 'John','password': 'seCreT'}
config['user.deets']['nickname'] = 'j'
with open('config.cfg', 'w') as configfile:
    config.write(configfile)


import configparser
config = configparser.ConfigParser()
config.read('config.cfg')
config.sections()
