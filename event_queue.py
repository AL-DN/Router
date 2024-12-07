from event_object import EventObj

class EventQueue:
    def __init__(self):
        self.events = []

    # returns # events 
    def count(self):
        return len(self.events)
    
    # places event into queue based on time
    def enqueue(self, event: EventObj):

        if len(self.events)==0:
            self.events.append(event)
            return

        for i in range(len(self.events)):
            if i == len(self.events)-1:
                self.events.append(event)
                return
            elif event.event_time <= self.events[i].event_time:
                self.events.insert(i,event)
                return
            else:
                continue

       

    # removes and returns packet
    def dequeue(self):
        return self.events.pop(0)