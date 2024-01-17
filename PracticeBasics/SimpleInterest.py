"""
Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where,
P is the principal amount T is the time and R is the rate

Examples:

Input : P = 10000
        R = 5
        T = 5
Output :2500.0
We need to find simple interest on
Rs. 10,000 at the rate of 5% for 5
units of time.
"""

# Solution1
def simple_interest(p, t ,r):
    si = (p * t * r)/100
    return si
print(simple_interest(8, 6, 8))

# Solution2 taking inputs from user
def si(p, t, r):
    sim_int = (p * t * r)/100
    return sim_int

p = int(input("Enter principal amount: "))
t = int(input("Enter time: "))
r = int(input("Enter rate of interest: "))

print(si(p, t, r))