"""
Variables and Objects

a_list = [ 1, 'New York', 100]

(Note that an assignment statement is being used, so evaluation of the right
side of the clause takes precedence over the left side.)

- At first, an object (a list in this example) is created in the computer's
memory. Now the object has its identity;
- then the object is populated with other objects. Now our object has a value;
- finally a variable, which you should treat as a label or name binding, is
created, and this label refers to a distinct place in the computer memory.

The built-in id() function returns the 'identity' of an object. This is an
integer which is guaranteed to be unique and constant for this object during
its lifetime. Two objects with non-overlapping lifetimes may have the same
id() value.
"""

a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
