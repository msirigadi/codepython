"""
Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15
This should return 5,6,7 as indices containing number 15 in the array
"""
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    list_index = []

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if number_to_find == mid_number:
            list_index.append(mid_index)
            break

        if number_to_find < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    if len(list_index) != 0:
        i = mid_index - 1
        while i >= 0:
            if numbers_list[i] == number_to_find:
                list_index.append(i)
            else:
                break
            i-=1

        i = mid_index + 1
        while i < len(numbers_list) - 1:
            if numbers_list[i] == number_to_find:
                list_index.append(i)
            else:
                break
            i+=1
    else:
        return []

    list_index.sort()
    return list_index

if __name__ == "__main__":
    numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 14

    index = binary_search(numbers_list, number_to_find)
    print(f"{number_to_find} is found at index {index}")