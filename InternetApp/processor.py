class Processor:
    """A class to represent the Processor in a Web system"""

    def __init__(self, publisher, receiver):
        """Initializes the Processor object with the relevant attributes"""

        self.publisher = publisher
        self.receiver = receiver

    def packet_check(self):
        """Checks if Alice has packets and loads them into Bob"""

        if self.publisher.packet_check() > 0:

            self.receiver.load_packets(self.publisher.get_packets())
            self.publisher.clear_cache()
