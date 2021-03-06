# pylog
util to facilitate creation and use of a common logger across files, classes, projects

See https://docs.python.org/3/library/logging.html for more information about basic python logging

## Purpose and Intended Audience

Use of this module enables easy creation and use of a common logger throughout a python project. In addition, 
messages with levels `logging.DEBUG` and `logging.INFO` are now sent to stdout; levels `logging.WARNING` and above
are instead routed stderr.

## Requirements

    python >=3.7

## Installation and usage

in a suitable virtual env...
```
pip install pip install https://github.com/huit/pylog/archive/refs/tags/v0.0.2.tar.gz

import logging
# for convenient access to logging levels (NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL)
from pylog.pylog import get_common_logger_for_module, get_common_logging_format
# from within a file:
logger = get_common_logger_for_module(level=logging.INFO, module_name=__name__)
```
or
```
log_format = logging.Formatter("some logging format")
logger = get_common_logger_for_module(level=logging.INFO, module_name=__name__, log_format=log_format)
```
The default logging format is:
```
'{"log_level": "%(levelname)s", "app_file_line": "%(name)s:%(lineno)d", "message": %(message)s}'
```
