"""
Objectives
improving the student's skills in operating with metaclasses;
improving the student's skills in operating with class variables and
class methods.

Scenario
* Imagine you’ve been given a task to clean up the code of a system developed
in Python – the code should be treated as legacy code;
* the system was created by a group of volunteers who worked with no clear
“clean coding” rules;
* the system suffers from a problem: we don’t know in which order the classes
are created, so it causes multiple dependency problems;
* your task is to prepare a metaclass that is responsible for:
    - equipping all newly instantiated classes with time stamps, persisted in a
    class attribute named instantiation_time;
    - equipping all newly instantiated classes with the get_instantiation_time()
    method. The method should return the value of the class attribute
    instantiation_time.

* The metaclass should have its own class variable (a list) that contains a
list of the names of the classes instantiated by the metaclass
(tip: append the class name in the __new__ method).

- Your metaclass should be used to create a few distinct legacy classes;
- create objects based on the classes;
- list the class names that are instantiated by your metaclass.
"""

import time

def get_class_instantiation_time(self):
    return self.class_instantiation_time

class CleanCodeGuard(type):
    classes_created = []

    def __new__(mcs, name, bases, dictionary):
        if 'get_class_instantiation_time' not in dictionary:
            dictionary['get_class_instantiation_time'] = get_class_instantiation_time

        obj = super().__new__(mcs, name, bases, dictionary)
        obj.class_instantiation_time = time.time()
        CleanCodeGuard.classes_created.append(name)
        time.sleep(1)
        return obj

class My_class1(metaclass=CleanCodeGuard):
    pass

class My_class2(metaclass=CleanCodeGuard):
    pass

my_object1 = My_class1()
print(my_object1.get_class_instantiation_time())
print(My_class1.__dict__)
print(my_object1.__dict__)

my_object2 = My_class2()
print(my_object2.get_class_instantiation_time())
print(My_class2.__dict__)
print(my_object2.__dict__)

print(CleanCodeGuard.classes_created)