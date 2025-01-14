"""
The Logger object allows you to create logs with different levels of logging
that help you to distinguish between less important logs and those reporting a
serious error. By default, the following logging levels are defined:

Level name	Value
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
Each level has a name and a numeric value. You can also define your own level,
but those offered by the logging module are quite sufficient. The Logger object
has methods that set the logging level for you.

You’re probably wondering why messages with INFO and DEBUG levels are not
displayed. This is due to the default configuration
"""

import logging

logging.basicConfig()

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARN message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

