from alice import Alice 
from bob import Bob 
from packet import Packet 
from processor import Processor 



if __name__ == "__main__":
    """
    Creates a Bob, Alice and Processor object then runs the entire program. Essentially, the flow will go as follows:

        1. Alice creates a packet and sends it to the Processor.
        2. Bob listens to the Processor and receives any available packets.
        3. Bob will read the packet then delete it.
    """


    alice = Alice()
    bob = Bob()
    processor = Processor(alice, bob)

    while True: 

        alice.work()
        processor.packet_check()
        bob.read_packets()