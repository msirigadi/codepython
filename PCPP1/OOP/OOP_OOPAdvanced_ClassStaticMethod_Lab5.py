"""
Objectives
improving the student's skills in operating with static and class methods

Scenario
- Create a class representing a luxury watch;
- The class should allow you to hold a number of watches created in the
watches_created class variable. The number could be fetched using a class
method named get_number_of_watches_created;
- the class may allow you to create a watch with a dedicated engraving (text).
As this is an extra option, the watch with the engraving should be created
using an alternative constructor (a class method), as a regular __init__ method
should not allow ordering engravings;
- the regular __init__ method should only increase the value of the appropriate
class variable;

The text intended to be engraved should follow some restrictions:
- it should not be longer than 40 characters;
- it should consist of alphanumerical characters, so no space characters are
allowed;
- if the text does not comply with restrictions, an exception should be raised;

before engraving the desired text, the text should be validated against
restrictions using a dedicated static method.

- Create a watch with no engraving
- Create a watch with correct text for engraving
- Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the
exception
- After each watch is created, call class method to see if the counter variable
was increased

"""

class LuxuryWatch:
    __watches_created = 0

    def __init__(self):
        LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @classmethod
    def create_watch_with_engraving(cls, text):
        if cls.validate_text(text):
            _watch = cls()
            _watch.engrave = text
            return _watch
        else:
            raise Exception(text + 'it does not follow the "alphanum" rule')

    @staticmethod
    def validate_text(text):
        if len(text) > 40 or not text.isalnum():
            return False
        else:
            return True

watch1 = LuxuryWatch()
print('No of watches created:', LuxuryWatch.get_number_of_watches_created())
watch2 = LuxuryWatch.create_watch_with_engraving('Mahi123')
print('No of watches created:', LuxuryWatch.get_number_of_watches_created())
try:
    watch3 = LuxuryWatch.create_watch_with_engraving('foo@baz.com')
except Exception as e:
    print('The problem is:', e)
    
print('No of watches created:', LuxuryWatch.get_number_of_watches_created())




