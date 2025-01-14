"""
Class variables and instance variables are often utilized at the same time, but
for different purposes. As mentioned before, class variables can refer to some
meta information or common information shared amongst instances of the same
class.

The example below demonstrates both topics: each class owns a counter variable
that holds the number of class instances created. Moreover, each class owns
information that helps identify the class instance origins. Similar
functionality could be achieved with the isinstance() function, but we want to
check if class variables can be helpful in this domain.

Both the Duck and Chicken classes own a class variable named species, which
holds a value unique to each class. When we iterate over all objects, we can
examine the value of this variable to take appropriate action.
"""

class Duck:
    counter = 0
    species = 'duck'

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        pass

    def quack(self):
        print('quacks')


class Chicken:
    species = 'chicken'

    def walk(self):
        pass

    def cluck(self):
        print('clucks')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print('so many ducks were born:', Duck.counter)

for poultry in duckling, drake, hen, chicken:
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    else:
        poultry.cluck()