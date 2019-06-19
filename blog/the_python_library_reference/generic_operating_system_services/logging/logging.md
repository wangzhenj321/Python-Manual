## Standard levels

1. DEBUG: `debug()`
2. INFO: `info()`
3. WARNING: `warning()`
4. ERROR: `error()`
5. CRITICAL: `critical()`

## Default logger

1. The default logger is `root`.
2. The default format is the level name, logger name, and message seperated by a colon.
3. By default, the logging module logs the messages with a severity level of WARNING or above.

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

## References

1. [Logging in Python](https://realpython.com/python-logging/)
2. [Logging HOWTO](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
3. [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)
4. [Logging facility for Python](https://docs.python.org/3/library/logging.html)
5. [Logging configuration](https://docs.python.org/3/library/logging.config.html)
6. [Logging handlers](https://docs.python.org/3/library/logging.handlers.html)
