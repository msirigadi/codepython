# Bubble sort

list = [8, 10, 6, 2, 4]
lst_len = len(list)

while True:
    swapped = 0
    for i in range(lst_len - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            swapped += 1

    if swapped == 0:
        break

    print(list)
    lst_len -= 1

print("Sorted list: ", list)


