"""
Implement merge sort - O(nlogn)
"""

def merge_two_sorted_list(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)

if __name__ == "__main__":
    arr = [10,3,15,7,8,23,98,29]

    #arr = [2, 9, 15, 21, 27, 38, 44]
    print(merge_sort(arr))

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        print(merge_sort(arr))
