#!/usr/bin/env python3

import logging
import sys

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


class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)


def get_common_logger_for_module(module_name: str, level: int = 0, log_format: logging.Formatter = get_common_logging_format()) -> logging.Logger:
    """
    Creates and returns a new logger for a module
    level should be selected from logging.DEBUG, logging.INFO, etc.
    DEBUG and INFO will be output to stdout
    WARNING, ERROR, and CRITICAL will be output to stderr

    :param module_name:
    :param level: defaults to logging.NOTSET
    :param log_format: defaults to get_common_logging_format()
    :return:
    """
    module_logger = logging.getLogger(name=module_name)
    module_logger.setLevel(level=level)

    info_stream_handler = logging.StreamHandler(stream=sys.stdout)
    info_stream_handler.setFormatter(fmt=log_format)
    info_stream_handler.setLevel(level=logging.DEBUG)
    info_stream_handler.addFilter(InfoFilter())
    module_logger.addHandler(hdlr=info_stream_handler)

    stream_handler = logging.StreamHandler(stream=sys.stderr)
    stream_handler.setFormatter(fmt=log_format)
    stream_handler.setLevel(level=logging.WARNING)
    module_logger.addHandler(hdlr=stream_handler)

    return module_logger
