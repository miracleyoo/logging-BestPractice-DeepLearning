import logging

# use the file name as the logger name
logger = logging.getLogger(__name__)
logger.info('This is a log message from %s' % __name__)

def load_data():
    logger.info('Loading data...')
    logger.debug('Debugging data...')
    pass