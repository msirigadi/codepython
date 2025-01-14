"""
The more complex example that dynamically creates a fully functional class is
presented in the right pane.

As you can see, the Dog class is now equipped with two methods
(feed() and bark()) and the instance attribute age.
"""

def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal,), {'age':0, 'bark': bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()