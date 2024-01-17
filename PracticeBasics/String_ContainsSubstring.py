"""
This article will cover how to check if a Python string contains another string
or a substring in Python. Given two strings, check whether a substring is in
the given string.

Input: Substring = "geeks"
            String="geeks for geeks"
Output: yes
Input: Substring = "geek"
           String="geeks for geeks"
Output: yes
"""

# Solution1
sub_str = "geeks"
str = "geeks for geeks"

if sub_str in str:
    print("yes")
else:
    print("No")

# Solution 2
sub_str = "geeks"
str = "geeks for geeks"

if(str.find(sub_str) != -1):
    print("Yes")
else:
    print("No")

# solution3 using index
sub_str = "geks"
str = "geeks for geeks"
try:
    str.index(sub_str)
    print("Yes")
except:
    print("No")

# Solution 4

s="geeks for geeks"
s2="geeks"
x=list(filter(lambda x: (s2 in s),s.split()))

print(["yes" if x else "no"])

# Solution 5
from collections import Counter

# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + test_str)

# Words Frequency in String Shorthands
# using Counter() + split()
res = Counter(test_str.split())
print(res)

# Printing result
print("The words frequency : ", dict(res))
