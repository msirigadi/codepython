"""
Implement binary search using recusrion
"""

def binary_search(numbers_list, number_to_find, left_index, right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if number_to_find == mid_number:
        return mid_index

    if number_to_find < mid_number:
        right_index = mid_index - 1
    else:
        left_index = mid_index + 1

    return binary_search(numbers_list, number_to_find, left_index, right_index)


if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 15

    index = binary_search(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"{number_to_find} is found at index {index}")