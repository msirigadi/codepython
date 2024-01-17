"""
Given an array of integers, find the sum of its elements.

Examples:

Input : arr[] = {1, 2, 3}
Output : 6
Explanation: 1 + 2 + 3 = 6
"""

# Solution1

def soa(arr):
    sum = 0
    for elem in arr:
        sum += elem

    return sum

if __name__ == "__main__":
    arr = [1, 2, 3]
    print(soa(arr))


# Solution2 using inbuilt sum() func
arr = [10, 20, 20, 40, 50]

print("sum of elements in arr:", sum(arr))


# solution3 using enumerate

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    total = 0
    
    for index, elem in enumerate(arr):
        total += elem

    print("sum", total)