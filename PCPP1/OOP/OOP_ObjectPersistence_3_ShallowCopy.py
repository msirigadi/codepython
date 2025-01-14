"""
When you process the data, you’ll come to the point where you may want to have
distinct copies of objects that you can modify without automatically modifying
the original at the same time.

Let's have a look at the following code. Its intention is to:
- make a real, independent copy of a_list, (not just a copy reference).
Using [:], which is an array slice syntax, we get a fresh copy of the a_list
object;
- modify the original object;
- see the contents of both objects.

Pay attention to the code presented in the right pane, of which a_list is a
compound object (an object that contains other objects, like lists,
dictionaries, or class instances).

So, despite the fact that b_list is a copy of a_list, modifying b_list results
in a modification of the a_list object.

The explanation of the behavior presented on the previous page is:
- the 'a_list' object is a compound object;
- we’ve run a shallow copy that constructs a new compound object, b_list in our
example, and then populated it with references to the objects found in the
original;
- as you can see, a shallow copy is only one level deep. The copying process
does not recurse and therefore does not create copies of the child objects,
but instead populates b_list with references to the already existing objects.

a_list                  b_list
[0] -------> 10 <-------- [0]
[1] ------> banana <----- [1]
[2] ---> [997, 123] <---- [2]
"""


print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Part 3")
print("Let's modify b_list[0]")
b_list[0] = 20
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)