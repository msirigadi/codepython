"""
Write a Python program for a given multiple numbers and a number n,
the task is to print the remainder after multiplying all the numbers divided by n.

Examples:

Input: arr[] = {100, 10, 5, 25, 35, 14},
n = 11
Output: 9
Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

Input : arr[] = {100, 10},
n = 5
Output : 0
Explanation: 100 x 10 = 1000 % 5 = 0
"""

def find_remainder(arr, n):
    prod = 1
    for elem in arr:
        prod *= elem

    return prod % n

if __name__ == "__main__":
    arr = [100, 10, 5, 25, 35, 14]
    print(find_remainder(arr, 11))