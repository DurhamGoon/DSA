class Bob:

    def __init__(self):
        
        self.packet_storage = []

    def load_packets(self, packets):

        self.packet_storage.extend(packets)

    def read_packets(self):

        for p in self.packet_storage:
            
            packet_data = p.get_data()

            print(f"Bob says: Reading packet.")
            print(f"Packet says: {packet_data}")
            print(f"Bob says: Deleting packet")
            self.packet_storage.remove(p)
    
    