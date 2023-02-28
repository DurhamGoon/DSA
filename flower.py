class Flower:
    """It be flower doe"""

    def __init__(self, name, petal_number, color):
        self._name = name
        self._petal_number = petal_number
        self._color = color 


    def set_name(self, name):
        self._name = name 

    def set_petal_number(self, petal_number):
        self._petal_number = petal_number

    def set_color(self, color):
        self._color = color 

    def get_name(self):
        return self._name
    
    def get_petal_number(self):
        return self._petal_number
    
    def get_color(self):
        return self._color
    
    def pluck(self):
        if self._petal_number - 1 < 0:
            return("Goofy ahh. What you gonna pluck omegalul")
        else:
            self._petal_number -= 1
            return("Ouch. You hurt {}. :( They have {} petals left.".format(self._name, self._petal_number))