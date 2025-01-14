"""
Queue implementation using Deque
"""

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


q = Queue()
q.enqueue({'company': 'Walmart',
           'timestamp': '14 Jan, 5:30 AM',
           'price': 250})
q.enqueue({'company': 'Walmart',
           'timestamp': '14 Jan, 5:31 AM',
           'price': 251})
q.enqueue({'company': 'Walmart',
           'timestamp': '14 Jan, 5:32 AM',
           'price': 252})

print(q.buffer)
print(q.size())
print(q.is_empty())
q.dequeue()
q.dequeue()
print(q.buffer)
print(q.size())