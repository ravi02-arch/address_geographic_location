import errno
import logging.handlers
import os

base_path = os.path.dirname(os.path.abspath(__file__))

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


make_sure_path_exists(os.path.join(base_path, "../logs"))
LOG_FILENAME = os.path.join(base_path, "../logs/app.log")

logFormat = '%(asctime)s - [%(filename)s::%(lineno)d] - %(levelname)12s - %(threadName)22s  - %(funcName)s ' \
            '- %(message)s'
# Set up a specific logger with our desired output level
LOG_LEVEL = logging.DEBUG
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=4000000, backupCount=15)
handler.setFormatter(logging.Formatter(logFormat))

logger = logging.getLogger('Logger')

logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)
ch = logging.StreamHandler()
ch.setLevel(LOG_LEVEL)
# create formatter
formatter = logging.Formatter(logFormat)
# add formatter to ch
ch.setFormatter(formatter)
