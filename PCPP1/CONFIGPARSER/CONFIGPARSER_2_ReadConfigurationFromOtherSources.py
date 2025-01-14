"""
The configparser module enables configurations from various sources to be
read. One of them is a dictionary that we can load using the read_dict

The read_dict method accepts any dictionary whose keys are section names,
while the values include dictionaries containing keys and values. All
values read from the dictionary are converted to strings.

NOTE: The configparser module also has read_file and read_string methods
that allow you to read the configuration from an open file or string. You
can find more information about these methods in the documentation.
"""

import configparser

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'user',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}


config = configparser.ConfigParser()
config.read_dict(dict)

print('Sections:', config.sections(), '\n')
print('mariadb section:')
print("Host:", config['mariadb']['host'])
print("Database:", config['mariadb']['name'])
print("Username:", config['mariadb']['user'])
print("Password:x`", config['mariadb']['password'], '\n')
print('redisdb section:')
print("Host:", config['redis']['host'])
print("Port:", config['redis']['port'])
print("Database Number:", config['redis']['db'], '\n')