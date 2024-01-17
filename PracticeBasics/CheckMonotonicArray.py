"""
Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].

An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes).

Examples:
Input : 6 5 4 4
Output : true

Input : 5 15 20 10
Output : false
"""

# Solution1
def monotonic_decreasing(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] >= arr[i+1]:
            continue
        else:
            return False

    return True

def monotonic_increasing(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            continue
        else:
            return False

    return True
def monotonic(arr):
    res1 = monotonic_decreasing(arr)
    res2 = monotonic_increasing(arr)

    return res1 or res2

if __name__ == "__main__":
    arr = [6,5,4,4]
    print(monotonic(arr))

    arr2 = [5, 15, 20, 10]
    print(monotonic(arr2))

# Solution2 using extend() and sort()

arr = [7, 5, 4, 2, 1]
a,b = [], []
a.extend(arr)
b.extend(arr)

a.sort()
b.sort(reverse=True)
print(id(arr))
print(id(a))
print(id(b))
print(arr, a, b)

if arr == a or arr == b:
    print("Monotonic")
else:
    print("Non Monotonic")

# Solution3

def isMonotonic(A):
    return(all(A[i] >= A[i+1] for i in range(len(A)-1)) or
            all(A[i] <= A[i+1] for i in range(len(A)-1)))

A = [6, 5, 4, 4]
print(isMonotonic(A))