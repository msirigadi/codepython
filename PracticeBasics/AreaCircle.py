"""
The area of a circle can simply be evaluated using the following formula.

Area = pi * r2
where r is radius of circle
"""

# Solution1
def find_area(rad):
    pi = 3.142
    area = pi * (rad**2)
    return area

print("Area:", find_area(5))


# Solution2 using math library

import math

def area(r):
    return math.pi * pow(r, 2)

print("Area:", area(5))