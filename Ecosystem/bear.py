from animal import Animal
import random

class Bear(Animal):

    def __init__(self, river):
        super().__init__(river)

    def move(self):
        
        movement = random.randint(-1,1)
        if self.get_river[self.get_location() + movement].get_animal_type() == "Fish":
            
            self.set_location(self.get_river[self.get_location()])
            self.mate(Bear())

