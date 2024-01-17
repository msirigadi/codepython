"""
Given a positive integer N, The task is to write a Python program to check if the number is Prime or not in Python.

Examples:

Input:  n = 11
Output: True


Input:  n = 1
Output: False

Explanation: A prime number is a natural number greater than 1 that
 has no positive divisors other than 1 and itself.
  The first few prime numbers are {2, 3, 5, 7, 11, ….}.
"""

def check_prime(num):
    if num == 1:
        return False

    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    else:
        return True

num = 10
print(f"{num} is prime: {check_prime(num)}")