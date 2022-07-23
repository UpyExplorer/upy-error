# coding=utf-8

"""
Module Base
"""

import sys
import traceback

def format_exception(error):
    """Return the exception in readable form
    Args:
        error (class): Exception
    Returns:
        str: Traceback Error
    """
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    exception_str = exception_str[:-1]

    return exception_str
