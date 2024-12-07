# Author: Alden Sahi

class PacketQueue:
    def __init__(self):
        # packet queue
        self.packets = []

    # returns # packets 
    def count(self):
        return len(self.packets)
    
    # adds packet to end of queue
    def enqueue(self, packet):
        self.packets.append(packet)

    # removes and returns packet
    def dequeue(self):
        return self.packets.pop(0)