import logging, sys, os

def init_logging(logging_level, log_dir=None, log_file_mode='w'):
    """
    Initialize the logging system so that it can be used by other modules.
    Args:
        logging_level: The logging level. It can be either a string or a logging level object.
        log_dir: The directory where the log file will be saved. If None, the log file will not be saved.
        log_file_mode: The mode with which the log file will be opened. It can be either 'w' or 'a'.
    """
    assert log_file_mode in ['w', 'a'], 'log_file_mode must be either "w" or "a"'

    # If the logging level is a string, convert it to a logging level object
    if isinstance(logging_level, str):
        logging_level = getattr(logging, logging_level.upper())

    # Create a formatter for the logs
    formatter = logging.Formatter('>[%(asctime)s][%(levelname)s][%(name)s][#%(lineno)d]: %(message)s', datefmt='%Y-%m-%d_%H:%M:%S')

    handlers = []
    # Create a stream-based handler that writes the log entries into the standard output stream
    handler_stdout = logging.StreamHandler(sys.stdout)
    # Set the created formatter as the formatter of the handler    
    handler_stdout.setFormatter(formatter)
    # Set the logging level of the stream-based handler to the given logging level
    handler_stdout.setLevel(logging_level)
    handlers.append(handler_stdout)
    
    # Create another stream-based handler that writes the log entries into a file
    if log_dir is not None:
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, 'log.txt')
        handler_file = logging.FileHandler(log_file_path, mode=log_file_mode)
        # Set the created formatter as the formatter of the handler
        handler_file.setFormatter(formatter)
        handlers.append(handler_file)
    
    # Add the created handler to this logger
    logging.basicConfig(handlers=handlers, level=logging_level)
    logging.info('Logger initialized. Logging level: %s' % logging.getLevelName(logging_level))
    if log_dir is not None:
        logging.info('Stdout logs will be saved to %s' % log_file_path)


def _init_logger(): 
    """
    If you want to only init a logger instead of the basic config, use this function.
    This function is not a well-polished function and it's for reference only, so use it with caution.
    """
    #Create a logger named 'root'
    logger = logging.getLogger('root')
    #Set the threshold logging level of the logger to INFO
    logger.setLevel(logging.INFO)
    #Create a stream-based handler that writes the log entries    #into the standard output stream
    handler = logging.StreamHandler(sys.stdout)
    #Create a formatter for the logs
    formatter = logging.Formatter('>[%(asctime)s][%(levelname)s][%(name)s]: %(message)s', datefmt='%Y-%m-%d_%H:%M:%S')
    #Set the created formatter as the formatter of the handler    
    handler.setFormatter(formatter)
    #Add the created handler to this logger
    logger.addHandler(handler)
    logger.info('Logger initialized')