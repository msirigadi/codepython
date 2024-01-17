"""
Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by:

A = P(1 + R/100) t

Compound Interest = A – P

Where,
A is amount
P is the principal amount
R is the rate and
T is the time span
"""

# Solution1
def compound_interest(p, t ,r):
    a = p * pow((1 + r/100), t)
    ci = a - p
    return ci

print(compound_interest(10000, 10.25, 5))

# Solution2 without pow() function

def power(base, exp):
    po = 1
    while exp > 0:
        po *= base
        exp -= 1

    return po

def comp_int(p, t ,r):
    a = p * power((1 + (r/100)), t)
    ci = a - p
    return ci

print(comp_int(10000, 10.25, 5))