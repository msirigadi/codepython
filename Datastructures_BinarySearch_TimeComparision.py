"""
Compare time taken against linear search
"""

import time
def time_it(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(function.__name__ + " took " + str((end-start) * 1000) + " mil secs")
        return result

    return wrapper

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index

    return -1

@time_it
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
    #numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    #number_to_find = 21

    numbers_list = [i for i in range(1, 100000)]
    number_to_find = 100000


    index = linear_search(numbers_list, number_to_find)
    #print(f"{number_to_find} is found at index {index}")

    index = binary_search(numbers_list, number_to_find)
    #print(f"{number_to_find} is found at index {index}")