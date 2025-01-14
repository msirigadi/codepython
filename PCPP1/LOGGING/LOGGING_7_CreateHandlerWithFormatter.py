"""
In the first step you need to create a Formatter object by passing the format
you've defined to its constructor. In the example, we use the format defined in
one of the previous examples.

The next step is to set the formatter in the handler object. This is done using
the setFormatter method. After doing this, you can analyze your logs in the
prod.log file.
"""

import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod3.log', 'w')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARN message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')
