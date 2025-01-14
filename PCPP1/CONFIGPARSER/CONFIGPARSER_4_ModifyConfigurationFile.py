"""
A configuration loaded using the read method can also be modified. To change a
single option, simply set the new value to the appropriate key, and then save
the file using the write method
"""

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config['redis']['db'] = '1'

with open('config.ini', 'w') as configfile:
    config.write(configfile)