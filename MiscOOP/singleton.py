# modules are singleton in python because import onlu creates a single copy of each module

# What the Gang of Four’s original Singleton Pattern
# might look like in Python.

class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


# More pythonic
# Straightforward implementation of the Singleton Pattern

class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

log1 = Logger()
log2 = Logger()
print(log1, log2)
print(log1 is log2)