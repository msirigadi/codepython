"""
Python gives you the ability to create a class that inherits properties from
any Python built-in class in order to get a new class that can enrich the
parent's attributes or methods. As a result, your newly-created class has the
advantage of all of the well-known functionalities inherited from its parent or
even parents and you can still access those attributes and methods.

Later, you can override the methods by delivering your own modifications for
the selected methods.

In the following example, we’ll create an implementation of our own list class

Your new class will be based on the Python list implementation and will also
validate the type of elements that are about to be placed onto it.

Such a list can be used in an application that requires the list elements to be
of a specific type (integers in the ticketing example), and control over the
types of elements is given to the mechanisms of the new class.

As a result, when solving a domain problem, we focus on the problem and not on
type control.
"""

class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')

    def __setitem__(self, key, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, key, value)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, iterable):
        for element in iterable:
            IntegerList.check_value_type(element)

        list.extend(self, iterable)


int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 49
print('Inserting int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('8-10')
except ValueError:
    print('Appending string failed')

try:
    int_list[0] = '10/11'
except ValueError:
    print('Inserting string failed')

try:
    int_list.extend([997, '10/11'])
except ValueError:
    print('Extending with ineligible element failed')

print('Final result:', int_list)


