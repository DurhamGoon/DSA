from alice import Alice 
from bob import Bob 
from packet import Packet 
from processor import Processor 



if __name__ == "__main__":

    alice = Alice()
    bob = Bob()
    processor = Processor(alice, bob)

    while True: 

        alice.work()
        processor.packet_check()
        bob.read_packets()