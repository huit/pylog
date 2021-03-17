#!/usr/bin/env python3

import logging

#============================================================================================
# Logging
#============================================================================================

def get_common_logging_format():
    """
    returns a basic logging format displaying logging level, file name and line number, and message
    :return:
    """
    return logging.Formatter(
        '{"log_level": "%(levelname)s", '
        '"app_file_line": "%(name)s:%(lineno)d", '
        '"message": %(message)s}'
    )


def get_common_logger(module_name: str, level: int = 0, log_format: logging.Formatter = get_common_logging_format()) -> logging.Logger:
    """
    Creates and returns a new logger for a module
    level should be selected from logging.DEBUG, logging.INFO, etc.

    :param module_name:
    :param level: defaults to logging.NOTSET
    :param log_format: defaults to get_common_logging_format()
    :return:
    """
    module_logger = logging.getLogger(name=module_name)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=level)
    stream_handler.setFormatter(fmt=log_format)
    module_logger.addHandler(hdlr=stream_handler)
    module_logger.setLevel(level=level)
    return module_logger
