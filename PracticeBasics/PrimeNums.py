"""
Given two positive integers start and end.
The task is to write a Python program to print all Prime numbers in an Interval.

Definition: A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.
"""

# solution1

def prime_nums(x, y):
    lst = []

    for num in range (x, y+1):
        prime = True

        if num == 1:
            continue

        for j in range(2, num//2+1):
            print(num, " = ", j)
            if num % j == 0:
                prime = False
                break

        if prime:
            lst.append(num)

    return lst

start_range = 2
end_range = 11

print(prime_nums(start_range, end_range))
