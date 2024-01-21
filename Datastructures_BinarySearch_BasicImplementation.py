"""
Implement binary search technique
For applying binary search, all the elements must be sorted
"""

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if number_to_find == mid_number:
            return mid_index

        if number_to_find < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = binary_search(numbers_list, number_to_find)
    print(f"{number_to_find} is found at index {index}")