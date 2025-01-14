"""
Parsing the configuration file is extremely simple. First, we need to create
a ConfigParser object, which provides many useful methods for parsing data.
One of them is the read method, responsible for reading and parsing the
configuration file. In our example, we pass the config.ini filename to it,
but it's also possible to pass a list containing several files.

If all goes well, the read method returns a list of filenames that have been
successfully parsed.
"""

import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections: ', config.sections(), '\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', config['redis']['port'])
print('Database number:', config['redis']['db'], '\n')

