"""
There is a given array and split it from a specified position, and move the first part of the array add to the end.

Input : arr[] = {12, 10, 5, 6, 52, 36}
            k = 2
Output : arr[] = {5, 6, 52, 36, 12, 10}
Explanation : Split from index 2 and first
part {12, 10} add to the end .
"""

def split_arr(arr, n):
    for i in range(0, n):
        x = arr [0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]

        arr[-1] = x
        print(arr)

if __name__ == "__main__":
    arr = [12, 10, 5, 6, 52, 36]
    k = 2
    split_arr(arr, k)
    print("Array:", arr)

