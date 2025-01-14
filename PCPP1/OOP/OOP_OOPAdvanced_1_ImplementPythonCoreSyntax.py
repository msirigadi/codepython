"""
Python allows us to employ operators when applied to our objects, so we can use
core operators on our objects.

What does it mean to add two objects of the Person class? Well, it depends on
the domain of your application.

If you’re developing an application for an elevator, then you should remember
that every elevator has safety limits regarding the total weight it can lift.

In this case, the '+' operator, when applied to two objects, should mean: add
the weight attribute values and return the corresponding result.

If the total sum of the weights of the Person class objects does not exceed the
safety limit, your elevator should allow them to be lifted.

When called, functions and operators that state the core syntax are translated
into magic methods delivered by specific classes.

So Python knows what to do when the interpreter spots the '+' operator between
two strings or two integers, or even two Person class objects – it looks for
the magic method responsible for the called function or operator in order to
apply it to the operands (objects).

The '+' operator is in fact converted to the __add__() method and the len()
function is converted to the __len__() method. These methods must be delivered
by a class (now it’s clear why we treat classes as blueprints) to perform the
appropriate action.

Look at the following simple code:

number = 10
print(number + 20)

It is in fact translated to:

number = 10
print(number.__add__(20))
"""

class Person:
    def __init__(self, age, salary, weight):
        self.age = age
        self.salary = salary
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1+p2)
