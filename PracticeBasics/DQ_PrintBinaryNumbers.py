"""
Write a program to print binary numbers from 1 to 10 using Queue.
Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010

Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1.
4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.
"""

from DQ_CreateQueue import Queue


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue('1')

    for i in range(n):
        num = numbers_queue.front()
        numbers_queue.enqueue(num + '0')
        numbers_queue.enqueue(num + '1')
        print(num)
        numbers_queue.dequeue()

if __name__ == "__main__":
    produce_binary_numbers(10)




