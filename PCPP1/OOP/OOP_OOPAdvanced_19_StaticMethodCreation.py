"""
Static methods are methods that do not require (and do not expect!) a parameter
indicating the class object or the class itself in order to execute their code.

When can it be useful?
1. When you need a utility method that comes in a class because it is
semantically related, but does not require an object of that class to execute
its code;
2. consequently, when the static method does not need to know the state of the
objects or classes.

Convention
- To be able to distinguish a static method from a class method or instance
method, the programmer signals it with the @staticmethod decorator preceding
the class method definition.
- Static methods do not have the ability to modify the state of objects or
classes, because they lack the parameters that would allow this.
"""

class BankAccount:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:   
            return False

account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if BankAccount.validate(element):
        print('We can use', element, 'to create a bank account')
    else:
        print('The account number', element, 'is invalid')