import time
import threading
from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[0]
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

order_queue = Queue()

def place_order(orders):
    for order in orders:
        print(f"Placing order for: {order}")
        order_queue.enqueue(order)
        time.sleep(0.5)
    
def serve_order():
    time.sleep(1)
    while True:
        order = order_queue.dequeue()
        print(f"The order: {order} is ready!")
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target= place_order, args= (orders,))
    t2 = threading.Thread(target= serve_order)

t1.start()
t2.start()