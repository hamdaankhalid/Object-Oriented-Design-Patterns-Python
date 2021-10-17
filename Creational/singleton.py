class Borg:
    
    """Borg class making class attributes global"""

    _shared_state = {}

    def __init__(self):
        self.__dict__=self._shared_state # Make it an attribute dictionary


class Singleton(Borg): # inherits from Borg
    """This class now shared all its attributes among its carious instances"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        # returns the attribute dictionaryto print 
        return str(self._shared_state)

# Create singleton object and add our first acronym
x = Singleton(HTTP = "Hyper text transfer protocol")
# print object
print(x)

# Lets create another singleton and see how shared state persists
y = Singleton(Hk = "Hamdaa Khalid")
print(y)