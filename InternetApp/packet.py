class Packet:
    """A class to represent a unique Packet in the system"""

    def __init__(self, data):
        """Initializes the Packet object with the relevant attributes"""

        self._data = data

    def get_data(self):
        """Returns the data attribute from this class"""

        return self._data 
    
    def set_data(self, data):
        """Sets the data attribute for this class"""
        
        self._data = data 


