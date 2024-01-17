"""
Here we are going to see how we can rotate array with Python code.

Array Rotation:

1-2-3-4-5-6-7
2-3-4-5-6-7-1 (Left rotation by 1)
"""

# Solution1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    arr = arr[1:] + arr[0:1]
    print(arr)

# Solution2
def left_rotation(arr, n):
    temp = arr[:n]
    arr[:] = arr[n:] + temp
    return arr

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    print(left_rotation(array, 3))