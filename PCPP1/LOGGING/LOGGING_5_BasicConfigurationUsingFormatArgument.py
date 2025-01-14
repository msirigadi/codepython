"""
The basicConfig method presented earlier can also be used to change the default
log formatting. This is done using the format argument, which can be defined
using any characters or attributes of the LogRecord object. Let's explain it
with the example in the editor.

Result in the prod.log file:

root:CRITICAL:2019-10-10 17:16:46,293:Your CRITICAL message

The format we define is created by combining the attributes of the LogRecord
object separated by a colon. The LogRecord object is automatically created by
the logger during logging. It contains many attributes, such as the name of the
logger, the logging level, or even the line number in which the logging method
is called. A full list of all available attributes can be found here
[https://docs.python.org/3/library/logging.html#logrecord-attributes]
"""

import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
logging.basicConfig(level=logging.ERROR, filename='prod1.log', filemode='a', format=FORMAT)

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARN message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')