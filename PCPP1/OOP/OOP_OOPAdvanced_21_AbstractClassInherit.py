"""
inherit the abstract class and forget about overriding the abstract method by
creating a RedField class that does not override the hello method.

- it’s possible to instantiate the GreenField class and call the hello method;
- the RedField class is still recognized as an abstract one, because it inherits
all elements of its super class, which is abstract, and the RedField class does
not override the abstract hello method.
"""

import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field')

class RedField(BluePrint):
    def yellow(self):
        pass

gf = GreenField()
gf.hello()

rf = RedField()