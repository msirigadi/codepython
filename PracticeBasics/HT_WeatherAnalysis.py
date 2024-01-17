"""
nyc_weather.csv contains new york city weather for first few days in the month of January.

1. Write a program that can answer following,
 - What was the average temperature in first week of Jan
 - What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

"""

temp_arr = []

with open("nyc_weather.csv", "r") as f:
    count = 1
    for line in f:
        if count == 1:
            count += 1
            continue
        ln = line.strip()
        element = ln.split(',')
        print(element)
        temp_arr.append((int(element[1])))

def average_temp(temps):
    temp = 0
    for i in range(0, 7):
        temp += temps[i]

    return temp / 7

def max_temp(temps):
    max = 0
    for i in range(len(temps)):
        if temps[i] > max:
            max = temps[i]

    return max

if __name__ == __main__:
    print(temp_arr)
    print("Average temp in first week of Jan: ", average_temp(temp_arr))
    print("Max temp in first 10 days of Jan: ", max_temp(temp_arr))