## Standard levels

1. **DEBUG:** `debug()`
2. **INFO:** `info()`
3. **WARNING:** `warning()`
4. **ERROR:** `error()`
5. **CRITICAL:** `critical()`

> The default level is **WARNING**, which means that only events of this level and above will be tracked, unless the logging package is configured to do otherwise.

## Default logger

1. The default logger is `root`.
2. The default format is the level name, logger name, and message seperated by a colon.
3. By default, the logging module logs the messages with a severity level of **WARNING** or above.

## Samples of `Formatter`

Time of log with milliseconds:

```python
logging.Formatter('%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d,%H:%M:%S')
```

Time of log with timezone:

```python
logging.Formatter('%(asctime)s', datefmt='%Y-%m-%dT%H:%M:%S%z')
```

Log with the format of logger's name, log level, file name and line number:

```python
logging.Formatter('%(name)s %(levelname)s %(filename)s:%(lineno)d')
```

## Multiple handlers and formatters

```python
import logging

# create logger with 'simple_example'
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

## References

1. [Logging in Python](https://realpython.com/python-logging/)
2. [Logging HOWTO](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
3. [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)
4. [Logging facility for Python](https://docs.python.org/3/library/logging.html)
5. [Logging configuration](https://docs.python.org/3/library/logging.config.html)
6. [Logging handlers](https://docs.python.org/3/library/logging.handlers.html)
