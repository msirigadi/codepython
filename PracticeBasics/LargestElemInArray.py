"""
To find the largest element in an array, iterate over each element and compare
it with the current largest element. If an element is greater, update the largest element.
At the end of the iteration, the largest element will be found.

Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20
Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
"""

# Solution1

def largest(arr):
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max

if __name__ == "__main__":
    arr = [10, 20, 4]
    print("Largest elem in arr:", largest(arr))

    arr2 = [20, 10, 20, 4, 100]
    print("Largest:", largest(arr2))


# Solution2 using built-in max func
if __name__ == "__main__":
    arr = [67, 23, 972, 28, 12 , 2,545]
    print("Largest:", max(arr))

# Solution3 using sort() function
if __name__ == "__main__":
    arr = [1,45,65,8,7,2,343,6686,0]
    arr.sort()
    print("Largest:", arr[-1])


# Solution4 using lambda
if __name__ == "__main__":
    arr = [5, 67,23,456, 1, 90]

    lar = max(arr, key = lambda x: x)
    print("Largest:", lar)