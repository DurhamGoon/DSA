import random

class River:

    def __init__(self):
        
        self._river = []

    def populate(self, bear, fish):

        elements = [bear, fish, None]

        for n in random.randint(50,100):

            self._river.append(random.choice(elements))

    def get_river(self):

        return self._river
    
    
