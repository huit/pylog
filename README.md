# pylog
util to facilitate creation and use of a common logger across files, classes, projects

See https://docs.python.org/3/library/logging.html for more information about basic python logging

## Requirements
    python >=3.7

## Installation and usage

    in a suitable virtual env...
    pip install pip install https://github.com/huit/pylog/archive/v1.0.0.tar.gz

    import logging
    # for convenient access to logging levels (NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL)
    from pylog.pylog import get_common_logger, get_common_logging_format
    # from within a file:
    logger = get_common_logger(logging.INFO, __name__)
    or
    log_format = logging.Formatter("some logging format")
    logger = get_common_logger(logging.INFO, __name__, log_format)

The default logging format is:

    '{"log_level": "%(levelname)s", "app_file_line": "%(name)s:%(lineno)d", "message": %(message)s}'
