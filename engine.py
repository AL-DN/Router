class Engine:
    def __init__(self, service_time, busy=False):
        # how long it takes to process a packet
        self.service_time = service_time
        # signals a packet is currently being processed and cannot allow more
        self.busy = busy