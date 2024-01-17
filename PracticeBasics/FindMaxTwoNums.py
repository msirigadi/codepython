"""
Find max of two nums
"""

# Solution1

def maximum(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

num1 = 10
num2 = 20

print("Max is", maximum(num1, num2))

# Solution2 using max() function

num1 = 5
num2 = 55

print("Max:", max(num1, num2))

# Solution3 using itenary operator

num1 = 67
num2 = 97

max = num1 if num1 > num2 else num2
print("Max:", max)

# Solution4 using lambda

num1 = 1
num2 = 2

max = lambda num1, num2: num1 if num1 > num2 else num2
print("Max:", max(num1, num2))

num1 = 25
num2 = 35

# Solution5 using list comprehension
max = [num1 if num1 > num2 else num2]
print("Max:", max)

# Solution6 using sort()

a = 20
b = 45

lst = [a,b]
lst.sort()
max = lst[-1]
print("Max:", max)

