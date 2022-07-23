# coding=utf-8

"""
Module Base
"""

import sys
import traceback

from .config import Style, logging, separator


def format_exception(error: Exception, log: bool = False):
    """Return the exception in readable form
    Args:
        error (class): Exception
        log (class): bool
    Returns:
        str: Traceback Error
    """

    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(
        traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(
        traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "UpyError: \n"
    exception_str += "".join(exception_list)
    exception_str = exception_str[:-1]

    message = "\n" + Style.RED + exception_str + Style.WHITE + Style.END

    if log:
        separator()
        logging.error(message)
        separator()

    return message
