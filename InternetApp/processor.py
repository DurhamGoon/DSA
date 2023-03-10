class Processor:

    def __init__(self, publisher, receiver):

        self.publisher = publisher
        self.receiver = receiver

    def packet_check(self):

        if self.publisher.packet_check() > 0:

            self.receiver.load_packets(self.publisher.get_packets())
            self.publisher.clear_cache()
