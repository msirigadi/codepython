"""
Duck typing is another way of achieving polymorphism, and represents a more
general approach than polymorphism achieved by inheritance. When we talk about
inheritance, all subclasses are equipped with methods named the same way as the
methods present in the superclass.

In duck typing, we believe that objects own the methods that are called. If
they do not own them, then we should be prepared to handle exceptions.

Let's talk about two things that share conceptually similar methods, but
represent totally different things, like cheese and wax. Both can melt, and we
use the melted forms for different purposes.

Both the Wax and Cheese classes own melt() methods, but there is no relation
between the two. Thanks to duck typing, we can call the melt() method.
Unfortunatelly, the Wood class is not equipped with this method, so an
AttributeError exception occurs.

Summary:
- polymorphism is used when different class objects share conceptually similar
methods (but are not always inherited)
- polymorphism leverages clarity and expressiveness of the application design
and development;
- when polymorphism is assumed, it is wise to handle exceptions that could
pop up.
"""

class Wax:
    def melt(self):
        print('Wax can be used to form a tool')
class Cheese:
    def melt(self):
        print('Cheese can be eaten')

class Wood:
    def fire(self):
        print('A fire has been started')

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except:
        print('No melt() method')