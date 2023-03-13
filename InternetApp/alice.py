import time
from packet import Packet

class Alice:
    """A class to represent Alice. She creates packets and sends them to Bob."""
    
    def __init__(self): 
        """Packet storage stores Packet objects. Counter is an ID for various packets."""

        self.packet_storage = []
        self.counter = 0

    def create_packet(self, counter):
        """Creates packet objects using an incremental label"""

        temp_packet = Packet(f"Packet {counter}")
        self.increment_counter()
        return temp_packet

    def store_packet(self, packet):
        """Stores each Packet object in the packet storage"""

        self.packet_storage.append(packet)
             
    def packet_check(self):
        """Checks the length of the packet_storage list"""
        
        return len(self.packet_storage)
    
    def clear_cache(self):
        """Clears the packet_storage list"""

        self.packet_storage.clear()
    
    def increment_counter(self):
        """Increments the counter attribute"""

        self.counter += 1

    def get_counter(self):
        """Returns the counter attribute"""

        return self.counter
    
    def get_packets(self):
        """returns the packet_storage attribute"""

        return self.packet_storage
    
    def work(self):
        """Creates a packet and stores it"""

        self.store_packet(self.create_packet(self.get_counter()))
        time.sleep(60)


    

        

    