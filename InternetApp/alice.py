import time
from packet import Packet

class Alice:

    

    def __init__(self):

        self.packet_storage = []
        self.counter = 0

    def create_packet(self, counter):

        temp_packet = Packet(f"Packet {counter}")
        self.increment_counter()
        return temp_packet

    def store_packet(self, packet):
        
        self.packet_storage.append(packet)
             
    def packet_check(self):

        return len(self.packet_storage)
    
    def clear_cache(self):

        self.packet_storage = []
    
    def increment_counter(self):

        self.counter += 1

    def get_counter(self):
        
        return self.counter
    
    def get_packets(self):

        return self.packet_storage
    
    def work(self):

        self.store_packet(self.create_packet(self.get_counter()))
        time.sleep(60)


    

        

    