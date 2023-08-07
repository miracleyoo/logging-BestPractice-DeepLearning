import logging

# use the file name as the logger name
logger = logging.getLogger(__name__)
logger.info('This is a log message from %s' % __name__)

def predict():
    logger.info('Predicting...')
    pass