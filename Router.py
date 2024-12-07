# Author: Alden Sahi
# Date: 12/06/2024
# Project Description: to determine the average wait time for packets, the number of
# packets that are dropped by the router, and the overall utilization of the router.


from packet_queue import PacketQueue
from event_object import EventObj
from event_queue import EventQueue

queue = EventQueue()
event=EventObj(event_time=1,event_type=0)
queue.enqueue(event)
for i in range(len(queue.events)):
    print(queue.events[i].event_time)
print("\n")

event=EventObj(event_time=3,event_type=0)
queue.enqueue(event)
for i in range(len(queue.events)):
    print(queue.events[i].event_time)
print("\n")

event=EventObj(event_time=7,event_type=0)
queue.enqueue(event)
for i in range(len(queue.events)):
    print(queue.events[i].event_time)
print("\n")

event=EventObj(event_time=2,event_type=0)
queue.enqueue(event)
for i in range(len(queue.events)):
    print(queue.events[i].event_time)
print("\n")

event=EventObj(event_time=1,event_type=0)
queue.enqueue(event)
for i in range(len(queue.events)):
    print(queue.events[i].event_time)
print("\n")

    

    



