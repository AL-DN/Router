# Author: Alden Sahi
# Date: 12/06/2024
# Project Description: to determine the average wait time for packets, the number of
# packets that are dropped by the router, and the overall utilization of the router.


from packet_queue import PacketQueue

queue = PacketQueue()
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)

for i in range(queue.count()):
    print(queue.dequeue())
    

    



