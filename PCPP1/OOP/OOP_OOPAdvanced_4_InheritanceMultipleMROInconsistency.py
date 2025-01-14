"""
MRO can report definition inconsistencies when a subtle change in the class D
definition is introduced, which is possible when you work with complex class
hierarchies.

Imagine that you have changed the class D definition from:

class D(B, C):
    pass

to:

class D(A, C):
    pass
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

class D(A, C):
    pass

D().info()