"""
Build a metaclass responsible for completing classes with a method (if missing)
to ensure that all your classes are equipped with a method named 'greetings'.

As you can see, there is a greetings() function defined that greets everyone
who interacts with it. In a real-life scenario, it could be a function that is
obligatory for every class and is responsible for the consistency of object
attributes; it could be a function returning a checksum for some of an
attribute's values.

In My_Class1, by design, there is no greetings function, so when the class is
constructed, it is equipped with a default function by the metaclass.

In contrast, in My_Class2 the greetings function is present from the very
beginning.

Both classes rely on the same metaclass.

When you run the code, you'll see that both class instances are equipped with
greetings() methods
"""

def greetings(self):
    print('Just a greeting function, but it could be something more serious '
          'like a checksum')

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()