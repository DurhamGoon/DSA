from animal import Animal
import random

class Fish(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._animal_type = "Fish"


    def move(self):
        
        movement = random.randint(-1,1)
        if self.get_river[self.get_location() + movement] == "Fish":
            self.set_location(self.get_river[self.get_location()])
            self.mate(Fish())


    def get_animal_type(self):
        return super().get_animal_type()
    
    def get_location(self):
        return super().get_location()