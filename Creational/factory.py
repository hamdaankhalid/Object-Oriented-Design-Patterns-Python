# Scenario: Our pet shop was only selling dogs, but now needs to send cats too.

class Dog:

    """A simple Dog class"""

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Woof!"

class Cat:

    """A simple Dog class"""

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"



def get_pet(pet="dog"):

    """The Factory method"""

    pets = dict(dog=Dog("Shadow"), cat=Cat("Spark"))

    return pets[pet]


c = get_pet(pet="cat")
d = get_pet(pet="dog")

print(c.speak())
print(d.speak())