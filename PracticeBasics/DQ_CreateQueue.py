"""
Implement Queue data structure
"""

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def isempty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    for elem in q.buffer:
        print(elem)

    print("Item popped: ", q.dequeue())
    print("Length of queue: ", q.size())
    print("Is q empty? ", q.isempty())
    print("Item popped: ", q.dequeue())
    print("Item popped: ", q.dequeue())
