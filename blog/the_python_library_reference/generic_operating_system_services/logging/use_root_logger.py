import logging

def use_root_logger():
    """Use the default logger 'root' to print simple logs.
    
    1. The 'logging' module provides the default logger 'root'.
    2. The default format of the logger 'root' is the severity level, 
    the logger name, and message separated by a colon.
    3. By default, the 'logging' module logs the messages with a 
    severity level of WARNING or above.
    
    The defined levels are:
    1. DEBUG
    2. INFO
    3. WARNING
    4. ERROR
    5. CRITICAL
    """
    logging.debug('This is a debug message.')
    logging.info('This is an info message.')
    logging.warning('This is a warning message.')
    logging.error('This is an error message.')
    logging.critical('This is a critical message.')

def use_basicConfig():
    """Use the 'basicConfig()' method to configure the logging.

    Some of the commonly used parameters for 'basicConfig(**kwargs)' 
    are:
    1. level
    2. filename
    3. filemode
    4. format

    It should be noted that calling 'basicConfig()' to configure the 
    'root' logger works only if the 'root' logger has not been 
    configured before. Basically, this function can only be called once.

    'debug()', 'info()', 'warning()', 'error()', and 'critical()' also 
    call 'basicConfig()' without arguments automatically if it has not 
    been called before. This means that after the first time one of the 
    above functions is called, you can no longer configure the 'root' 
    logger because they would have called the 'basicConfig()' function 
    internally.
    """
    logging.basicConfig(filename='app.log', filemode='w', 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
        datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('This will get logged to a file.')

    # log variable data
    logging.warning('The module name is %s.', __name__)
    logging.warning(f'{__name__} is the module name.')

    # capture stack trace
    try:
        1 / 0
    except:
        logging.error("Exception occured", exc_info=True)

if __name__ == '__main__':
    # use_default_root_logger()
    # print(use_default_root_logger.__doc__)
    # print(use_basicConfig.__doc__)
    use_basicConfig()
