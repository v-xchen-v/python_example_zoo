"""Share logger to log message with the same config from another python file"""
from custom_logger import logger
logger.critical('use share logger by create a logger in separate module')