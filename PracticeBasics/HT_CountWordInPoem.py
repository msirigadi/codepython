"""
poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
You have to read this file in python and print every word and its count as show below.
Think about the best data structure that you can use to solve this problem and
figure out why you selected that specific data structure.

 'diverged': 2,
 'in': 3,
 'I': 8
"""
import re

poem_dict = {}

with open("poem.txt", "r") as f:
    for line in f:
        ln = re.sub(",|;|—|:|!|\.", " ", line)
        for word in ln.split():
            if word not in poem_dict:
                poem_dict[word] = 1
            else:
                poem_dict[word] += 1

print(poem_dict)
