# coding=utf-8

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.WARN
)

class Style():
    """
    A simple color class
    """

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'
    END = '\033[0m'


def separator():
    """
    Function to separate line
    """
    print(chr(61)*42)
