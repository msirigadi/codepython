"""
Implement stack DS
"""

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

if __name__ == '__main__':
    st = Stack()
    print(st.container)
    st.push(10)
    st.push(20)
    st.push([30, 40])
    st.push(75)
    print(st.container)
    print("Last inserted value: ", st.peek())
    print("Is stack empty? ", st.is_empty())
    print("Size of stack: ", st.size())
    st.pop()
    print(st.container)
    st.pop()
    print(st.container)