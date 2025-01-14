"""
Stack implementation using Deque

Stack can be implemented using list which is dynamic array in python.
But when the element to be added does not have memory in dynamic array,
the whole list has to be re-alloacted and all the elements has to be
copied to new memory location. This is overhead

Deque is a double linked list implementation which can be used to create
stack and avoid the overhead caused with dynamic list
"""

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()
s.push(10)
s.push(20)
print("Topmost element", s.peek())
print("Len of stack", s.size())
print("Is stack empty?", s.is_empty())
s.pop()
print("Len of stack", s.size())
print(s)