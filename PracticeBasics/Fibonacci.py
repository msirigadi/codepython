"""
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

Fn = Fn-1 + Fn-2
With seed values

F0 = 0 and F1 = 1.
"""

# Solution1 using recursion

def Fibonacci(num):
    if num == 1:
        return 0

    if num == 2:
        return 1

    return Fibonacci(num-1) + Fibonacci(num-2)

num = 10

print(" Fibonacci of {} is {}".format(num, Fibonacci(num)))

# Solution2 using dynamic programming

fib_array = [0, 1]

def fibonacci(num):
    if num <= 0:
        print("Incorrect input")
    elif num <= len(fib_array):
        return fib_array[num -1]
    else:
        temp = fibonacci(num -1) + fibonacci(num - 2)
        fib_array.append(temp)
        return temp

print(fibonacci(10))