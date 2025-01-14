"""
The “Integer only list” is an example of the employment of a subclassed
built-in list to check the types of elements being added to the list. How about
checking the values of the keys being used when new elements are added to the
dictionary?

For those of you who have taken the course “Programming Essentials in Python”,
the IBAN Validator should be well know. But, if you haven’t taken the course,
now is a good moment familiarize yourself with IBAN and ways to validate it.

We'll use the IBAN Validator to ensure that our banking app dictionary contains
only validated IBANs (keys) and info about the associated balance (value).

An IBAN-compliant account number consists of:
- a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for
France, GB for the United Kingdom, DE for Germany, and so on)
- two check digits used to perform the validity checks – fast and simple, but
not fully reliable, tests, showing whether a number is invalid (distorted by a
typo) or seems to be good;
- the actual account number (up to 30 alphanumeric characters – the length of
that part depends on the country)
"""

import random


class IBANValidationError(Exception):
    pass


class IBANDict(dict):
    def __setitem__(self, _key, _val):
        if validateIBAN(_key):
            super().__setitem__(_key, _val)

    def update(self, *args, **kwargs):
        for _key, _val in dict(*args, **kwargs).items():
            if validateIBAN(_key):
                super().__setitem__(_key, _val)

def validateIBAN(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


my_dict = IBANDict()
keys = ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']

for key in keys:
    my_dict[key] = random.randint(0, 1000)

print('The my_dict dictionary contains:')
for key, value in my_dict.items():
    print("\t{} -> {}".format(key, value))

try:
    my_dict.update({'dummy_account': 100})
except IBANValidationError:
    print('IBANDict has protected your dictionary against incorrect data insertion')
