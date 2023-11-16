"""Log messages at various levels"""
"""Log time with message"""
"""Log to file"""

import logging
def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="app_1116.log")

    logging.debug("This is a debug message.")
    logging.info("This is a info message.")
    logging.warning("This is a warning message.")
    logging.error("This is a error message.")
    logging.critical("This is a critical message.")


if __name__ == '__main__':
    main()
