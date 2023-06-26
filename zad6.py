import logging
import time
import datetime
from functools import wraps
import sys

def log(level=logging.DEBUG):
    def decorator(func):
        def wrapper(*args,):

            logger = logging.getLogger(func.__module__)
            logger.propagate=False

            result = func(*args)

            start_time = time.time()
            end_time = time.time()
            duration = end_time - start_time
            log_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setLevel(logging.DEBUG)
            stdout_handler.setFormatter(log_format)

            while logger.handlers:
               logger.handlers.pop()
               
            logger.addHandler(stdout_handler)

            logger.log(level, f"Nazwa funkcji: {func.__name__}  Argumenty wywołania: ({args})  Wartość zwracana: {result}  Czas wywołania:  {datetime.datetime.fromtimestamp(start_time)}   Czas trwania: {duration}s")

            return result
        return wrapper
    return decorator



