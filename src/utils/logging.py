# tasksigma/src/utils/logging.py

import logging
import logging.config

def setup_logging(log_level=logging.INFO, log_file=None):
    """
    Sets up logging configuration for the TaskSigma project.

    Args:
        log_level (int): Logging level (e.g., logging.DEBUG, logging.INFO).
        log_file (str, optional): Path to a file where logs should be written. If None, logs are only written to the console.

    Returns:
        None
    """
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': log_level,
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['console'],
                'level': log_level,
                'propagate': True
            },
        }
    }

    if log_file:
        logging_config['handlers']['file'] = {
            'level': log_level,
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': log_file,
        }
        logging_config['loggers']['']['handlers'].append('file')

    logging.config.dictConfig(logging_config)
    logging.info("Logging setup complete.")


def get_logger(name):
    """
    Retrieves a logger with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The logger instance.
    """
    return logging.getLogger(name)
