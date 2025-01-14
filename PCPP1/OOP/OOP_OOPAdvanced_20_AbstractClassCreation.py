"""
An abstract class should be considered a blueprint for other classes, a kind of
contract between a class designer and a programmer:

- the class designer sets requirements regarding methods that must be
implemented by just declaring them, but not defining them in detail. Such
methods are called abstract methods.
- The programmer has to deliver all method definitions and the completeness
would be validated by another, dedicated module. The programmer delivers the
method definitions by overriding the method declarations received from the class
designer.

This contract assures you that a child class, built upon your abstract class,
will be equipped with a set of concrete methods imposed by the abstract class.

Why do we want to use abstract classes?
The very important reason is: we want our code to be polymorphic, so all
subclasses have to deliver a set of their own method implementations in order
to call them by using common method names.

Furthermore, a class which contains one or more abstract methods is called an
abstract class. This means that abstract classes are not limited to containing
only abstract methods – some of the methods can already be defined, but if any
of the methods is an abstract one, then the class becomes abstract.

What is an abstract method?
An abstract method is a method that has a declaration, but does not have any
implementation. We'll give some examples of such methods to emphasize their
abstract nature.

Python has come up with a module which provides the helper class for defining
Abstract Base Classes (ABC) and that module name is abc.

The ABC allows you to mark classes as abstract ones and distinguish which
methods of the base abstract class are abstract. A method becomes abstract by
being decorated with an @abstractmethod decorator.
"""

import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to GreenField')

gf = GreenField()
gf.hello()

