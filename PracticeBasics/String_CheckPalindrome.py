"""
Given a string, write a python function to check if it is palindrome or not.
A string is said to be a palindrome if the reverse of the string is the same as
the string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

Examples:

Input : malayalam
Output : Yes

Input : geeks
Output : No
"""

#Solution1

string = "malayalam"
if string[::-1] == string:
    print("Palindrome")
else:
    print("Not palindrome")

# Solution2
string = "radar"
list_str = list(string)

str = ""

for i in range(len(list_str)):
    str += list_str.pop()

if str == string:
    print("Palindrome")
else:
    print("Non palindrome")

