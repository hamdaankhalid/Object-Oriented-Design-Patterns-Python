"""
Useful when the user expects to recieve a family of related objects, but doesnt need to know the type till runtime
Scenario: Pet Factory:
    - Dog factory
    - Cat factory

Solution
- Abstract Factory: pet factory
- Concrete Factory: cat and dog factory
- Abstract product
- Concrete product: dog and dog food, cat and cat food
"""

class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:

    def get_pet(self):
        # returns dog object
        return Dog()

    def get_food(self):
        # returns dog food object
        return "Dog food!"


class PetStore:
    # houses our abstract factories
    def __init__(self, pet_factory=None):
        # pet_factory is abstract factory
        
        self._pet_factory = pet_factory

    def show_pet(self):
        # utility method for printing

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}")
        print(f"Pet says {pet.speak()}")
        print(f"Pet eats {pet_food}")


factory = DogFactory()

# create a petsotre housing our abstract factory
shop = PetStore(factory)

shop.show_pet()

