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
        print("InfoFilter")
        print(f"\trec = {rec}")
        print(f"\trec.levelno = {rec.levelno}")
        pass_filter = rec.levelno in (logging.DEBUG, logging.INFO)
        print(f"\tpass_filter = {pass_filter}")
        return pass_filter


class WarningFilter(logging.Filter):
    def filter(self, rec):
        print("WarningFilter")
        print(f"\trec = {rec}")
        print(f"\trec.levelno = {rec.levelno}")
        pass_filter = rec.levelno in (logging.WARNING, logging.ERROR, logging.CRITICAL)
        print(f"\tpass_filter = {pass_filter}")
        return pass_filter


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

    info_stream_handler = logging.StreamHandler(sys.stdout)
    info_stream_handler.setFormatter(fmt=log_format)
    info_stream_handler.setLevel(level=logging.DEBUG)
    # info_stream_handler.addFilter(InfoFilter())
    module_logger.addHandler(hdlr=info_stream_handler)

    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(fmt=log_format)
    stream_handler.setLevel(level=logging.WARNING)
    info_stream_handler.addFilter(WarningFilter())
    module_logger.addHandler(hdlr=stream_handler)

    return module_logger
