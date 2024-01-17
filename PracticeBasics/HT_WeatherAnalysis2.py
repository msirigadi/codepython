"""
nyc_weather.csv contains new york city weather for first few days in the month of January.

2. Write a program that can answer following,
 - What was the temperature on Jan 9?
 - What was the temperature on Jan 4?
Figure out data structure that is best for this problem
"""

from HT_CreateHashTableWithCollision import Hashtable

ht = Hashtable()

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.rstrip().split(',')
        try:
            temperature = int(tokens[1])
            ht[tokens[0]] = temperature
        except:
            print("Invalid temperature. Skip the row")

ht.print()
print("Temperature on Jan 9: ", ht['Jan 9'])
print("Temperature on Jan 4: ", ht['Jan 4'])


