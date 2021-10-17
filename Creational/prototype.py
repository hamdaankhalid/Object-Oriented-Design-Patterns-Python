# When creating many identical objects indivudally is exensive, one could clone

import copy

class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
    
    def __str__(self):
        return str((self.name, self.color))

c = Car()

p = Prototype()

p.register_object('skylar', c)

c2 = p.clone('skylar')
c2.color = "black"

print(c)
print(c2)