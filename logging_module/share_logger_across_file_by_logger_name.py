"""Share logger to log message with the same config from another python file"""

import logging, custom_logger
logger = logging.getLogger('custom_logger')
logger.critical("use share logger with logger name directly")