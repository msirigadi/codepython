"""
You can derive any new class from more than one previously defined class.

But multiple inheritance should be used with more prudence than single
inheritance because:

- a single inheritance class is always simpler, safer, and easier to understand
and maintain;
- multiple inheritance may make method overriding somewhat tricky; moreover,
using the super() function can lead to ambiguity;
- it is highly probable that by implementing multiple inheritance you are
violating the single responsibility principle;

In our case:

class D does not define the method info(), so Python has to look for it in the
class hierarchy;
class D is constructed in this order:
    - the definition of class B is fetched;
    - the definition of class C is fetched;
Python finds the requested method in the class B definition and stops searching;
"""

class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()