import random

class Animal:

    def __init__(self, river):

        self._animal_type = ""
        self._location = 0
        self._river = river 

    def move(self):
        
        movement = random.randint(-1,1)
        pass
    
    def mate(self, animal):

        for spot in self.get_river():
            if spot == None:
                self.get_river[spot] = animal

    def get_location(self):

        return self._location
    
    def get_animal_type(self):

        return self._animal_type
    
    def set_location(self, location):

        self._location = location

    def get_river(self):
        
        return self._river
    
    def set_river(self,river):

        self._river = river 
    

