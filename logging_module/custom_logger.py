"""Seperate logs to different files"""
"""Trick: logging.getLogger(__name__) to create one logger for each Python module """

import logging

logging.basicConfig(level=logging.WARNING, filename='custom.log')
logger = logging.getLogger('custom_logger')