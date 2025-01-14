"""
Objectives
- improving the student's skills in operating with the getter, setter, and
deleter methods;
- improving the student's skills in creating their own exceptions.

Scenario
- Implement a class representing an account exception,
- Implement a class representing a single bank account,
- This class should control access to the account number and account balance
attributes by implementing the properties:
        - it should be possible to read the account number only, not change it.
        In case someone tries to change the account number, raise an alarm by
        raising an exception;
        - it should not be possible to set a negative balance. In case someone
        tries to set a negative balance, raise an alarm by raising an exception;
        - when the bank operation (deposit or withdrawal) is above 100.000,
        then additional message should be printed on the standard output
        (screen) for auditing purposes;
        - it should not be possible to delete an account as long as the balance
        is not zero;

test your class behavior by:
- setting the balance to 1000;
- trying to set the balance to -200;
- trying to set a new value for the account number;
- trying to deposit 1.000.000;
- trying to delete the account attribute containing a non-zero balance.
"""

class AccountException(Exception):
    pass

class BankAccount:
    def __init__(self, acc_no):
        self.__number = acc_no
        self.__balance = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, acc_no):
        raise AccountException('Account number cannot be changed')

    @number.deleter
    def number(self):
        raise AccountException('Invalid operation')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException('Cannot set negative value')

        if abs(self.__balance - value) > 100_000:
            print('This operation will be audited')

        self.__balance = value

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise AccountException('Cannot delete account as long it is not '
                                   'empty')

        self.__balance = None

    def __str__(self):
        return 'Account #{} balance is {}'.format(self.__number,
                                                  self.__balance)

account = BankAccount('34-3834-3435-5756-0001')
account.balance += 1000
print(account)

try:
    account.balance = -200
except AccountException as e:
    print('Exception detected:', e)

try:
    account.number = 'a new one'
except AccountException as e:
    print('Exception detected:', e)

try:
    account.balance += 1_000_000
except AccountException as e:
    print('Exception detected:', e)

try:
    del account.balance
except AccountException as e:
    print('Exception detected:', e)

