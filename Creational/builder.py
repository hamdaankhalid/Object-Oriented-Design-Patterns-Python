# Antipattern to solve when trying to build something with excessive number of constructors
"""
Director
Abstract Builder Interface
Convrete Builder implements interface
Product : object being built

Building a car from many small objects
"""

class Director():
    
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        print(self._builder.get_car())

class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()
    
    def get_car(self):
        return self.car

class SkyLarkBuilder(Builder):
    """Concrete Builder"""
    def add_model(self):
        self.car.model = "Skylark"
        
    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"

class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return str((self.model, self.tires, self.engine))


concrete_builder = SkyLarkBuilder()
director = Director(concrete_builder)

director.construct_car()
director.get_car()
