"""
The root logger has the logging level set to WARNING. This means that messages
at the INFO or DEBUG levels aren't processed.

Sometimes you may want to change this behavior, especially if you create your
own logger. To do this, you need to pass a logging level to the setLevel method.
"""

import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARN message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')