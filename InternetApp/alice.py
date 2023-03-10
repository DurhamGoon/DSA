import time
from packet import Packet

class Alice:
    counter = 0

    def __init__(self):
        self.packet_storage = []

    def create_packet(self, counter):
        
        return Packet()

    def store_packet(self, packet):
        self.packet_storage.append(packet)
             

    while True: 
        time.sleep(60)
        store_packet(create_packet(counter))

    