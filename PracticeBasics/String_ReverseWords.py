"""
We are given a string and we need to reverse words of a given string

Examples:

Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks
Input : str = "my name is laxmi"
output : str= laxmi is name my
"""

# Solution1

str ="geeks quiz practice code"
lst = str.split()[::-1]

print(" ".join(lst))

# Solution2 using stack

str = "my name is mahi"

stack = []

for elem in str.split():
    stack.append(elem)

reversed_lst =[]
while stack:
    reversed_lst.append(stack.pop())

print(" ".join(reversed_lst))