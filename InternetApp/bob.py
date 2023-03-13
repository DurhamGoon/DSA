class Bob:
    """A class to represent Bob. Bob receives packets from Alice and deletes them once read."""
    
    def __init__(self):
        """Initializes the Bob class with the proper attributes"""    

        self.packet_storage = []

    def load_packets(self, packets):
        """Loads the packets into Bob's storage to be read."""
        self.packet_storage.extend(packets)

    def read_packets(self):
        """Reads the packets in Bob's packet storage and deletes them"""

        for p in self.packet_storage:
            
            packet_data = p.get_data()

            print(f"Bob says: Reading packet.")
            print(f"Packet says: {packet_data}")
            print(f"Bob says: Deleting packet")
            self.packet_storage.remove(p)
    
    