"""
The big advantage of the configuration file is the possibility of using
interpolation. It allows you to create expressions consisting of a placeholder
under which the appropriate value will be substituted.

The configuration file has been extended with another option called dsn. Its
value contains the placeholder %(host)s, which needs to be replaced by an
appropriate value.

Placing any key between % and s informs the parser of the need to interpolate.
Of course, all the work is done for us, and we only get the ready results.

For the dsn option, it'll be the following string: redis://localhost. Note that
the placeholder %(host)s has been replaced by the value stored in the host option.
"""

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config['redis']['dsn'] = 'redis://{}'.format('%(host)s')

with open('config2.ini', 'w') as configfile:
    config.write(configfile)

print("dsn:", config['redis']['dsn'])