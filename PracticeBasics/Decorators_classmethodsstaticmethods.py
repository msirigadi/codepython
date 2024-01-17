"""
Create a class representing a luxury watch;
The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
the regular __init__ method should only increase the value of the appropriate class variable;
The text intended to be engraved should follow some restrictions:

it should not be longer than 40 characters;
it should consist of alphanumerical characters, so no space characters are allowed;
if the text does not comply with restrictions, an exception should be raised;
before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

Create a watch with no engraving
Create a watch with correct text for engraving
Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
After each watch is created, call class method to see if the counter variable was increased

"""


class Luxurywatch:
    __watches_created = 0

    def __init__(self):
        Luxurywatch.__watches_created += 1

    @classmethod
    def get_number_of_watches(cls):
        return Luxurywatch.__watches_created

    @classmethod
    def create_method_with_engraving(cls, text):

        try:
            cls.validate_text(text)
            _watch = cls()
            _watch.engrave = text
            return _watch
        except:
            print("Invalid text to engrave")

    @staticmethod
    def validate_text(text):
        if len(text) > 40 or not text.isalnum():
            raise Exception


lw1 = Luxurywatch()
"""
print(lw1._Luxurywatch__watches_created)
print(Luxurywatch._Luxurywatch__watches_created)
"""
print("Total num of watches {}".format(Luxurywatch.get_number_of_watches()))
lw2 = Luxurywatch.create_method_with_engraving("AtharvAndSrinuILoveYouBoth")
print("Total num of watches {}".format(Luxurywatch.get_number_of_watches()))
lw3 = Luxurywatch.create_method_with_engraving("foo@baz.com")
print("Total num of watches {}".format(Luxurywatch.get_number_of_watches()))



