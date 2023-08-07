import logging
from scripts.utils.logging_utils import init_logging
from scripts.models.v2ce import run_model
from scripts.data.dataset import load_data
from tools.pred import predict

init_logging('debug', log_dir='./logs')
_logger = logging.getLogger('main')

_logger.warning('This is a warning message')
_logger.error('This is an error message')
_logger.info('This is a log message')
_logger.debug('This is a debug message')

load_data()
run_model()
predict()