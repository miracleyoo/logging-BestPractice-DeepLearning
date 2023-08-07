import logging
import argparse

from scripts.utils.logging_utils import init_logging
from scripts.models.v2ce import run_model
from scripts.data.dataset import load_data
from tools.pred import predict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--logging_level', type=str, default='info',
                        help='The logging level. It can be either a string or a logging level object.')
    parser.add_argument('-d', '--log_dir', type=str, default='./logs',
                        help='The directory where the log file will be saved. If None, the log file will not be saved.')
    parser.add_argument('-m', '--log_file_mode', type=str, default='w',
                        help='The mode with which the log file will be opened. It can be either "w" or "a".')
    args = parser.parse_args()

    init_logging(args.logging_level, args.log_dir, log_file_mode=args.log_file_mode)
    logger = logging.getLogger('main')

    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.info('This is a log message')
    logger.debug('This is a debug message')

    load_data()
    run_model()
    predict()

# Please try the following commands and check the difference between the outputs:
# python main.py --logging_level info --log_dir ./logs
# python main.py --logging_level debug --log_dir ./logs