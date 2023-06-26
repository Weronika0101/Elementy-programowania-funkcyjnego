import logging
from zad6 import log

logging.basicConfig(level=logging.DEBUG)

@log(level=logging.INFO)
def my_function(arg1, arg2):
    return arg1 + arg2

@log(level=logging.DEBUG)
def my_function1(arg1, arg2):
    return arg1 - arg2

class SampleClass:
    @log(level=logging.DEBUG)
    def __init__(self, index):
        self.index = index

my_function(2,4)
my_function(3,4)
my_function1(3,4)

test= SampleClass(5)
