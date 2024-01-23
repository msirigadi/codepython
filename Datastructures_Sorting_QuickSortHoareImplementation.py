"""
Implement quick sort using hoare partitioning scheme
"""

def swap(a, b, elements):
    if a!=b:
        elements[a], elements[b] = elements[b], elements[a]

def partition(elements, left, right):
    pivot_index = left

    pivot_element = elements[pivot_index]

    while left < right:
        while left < right and elements[left] <= pivot_element:
            left += 1

        while elements[right] > pivot_element:
            right -= 1

        if left < right:
            swap(left, right, elements)

    swap(pivot_index, right, elements)
    return right

def quick_sort(elements, left, right):
    if left < right:
        partition_index = partition(elements, left, right)
        quick_sort(elements, left, partition_index-1)
        quick_sort(elements, partition_index+1, right)

if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    #elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    test = [[4, 89, 100, 34, 1, 27, 11, 88],
            [1, 2, 3, 4],
            [89, 87, 86, 85, 84],
            [10],
            [31, 21],
            [91, 2, 93],
            []]

    for elements in test:
        quick_sort(elements, 0, len(elements) - 1)

    for elem in test:
        print(elem)
