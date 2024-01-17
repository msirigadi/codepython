"""
Strings are data types used to represent text/characters. In this article,
we present different methods for the problem of removing the ith character from a
string and talk about possible solutions that can be employed in achieving them using Python.

Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.
"""

# Solution1

str = "Geeks123For123Geeks"
str_to_replace = "123"

print(str.replace(str_to_replace, ""))

# Solution using slice and pos
test_str = "GeeksForGeeks"
pos = 3
str = "".join([test_str[i] for i in range(len(test_str)) if i != pos-1])
print(str)


