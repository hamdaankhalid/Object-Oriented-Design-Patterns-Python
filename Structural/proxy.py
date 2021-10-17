"""
Client interacts with proxy till resource intensive object is available
"""
import time

class Producer:
    """
        Resource intensive object
    """
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Produver has time to meet you now")

class Proxy:
    """
        Relatively less resource intensive proxy to instantiate as a middleman
    """
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is busy!")

proxy = Proxy()

proxy.produce()

proxy.occupied = 'Yes'

proxy.produce()
