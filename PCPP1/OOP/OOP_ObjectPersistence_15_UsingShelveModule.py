"""
There is another handy module, called shelve, that is built on top of pickle,
and implements a serialization dictionary where objects are pickled and
associated with a key. The keys must be ordinary strings, because the
underlying database (dbm) requires strings.

Therefore, you can open your shelved data file and access your pickled objects
via the keys the way you do when you access Python dictionaries. This could be
more convenient for you when you’re serializing many objects.

Using shelve is quite easy and intuitive.

First, let's import the appropriate module and create an object representing a
file-based database:

import shelve
my_shelve = shelve.open('first_shelve.shlv', flag='w')

The meaning of the optional flag parameter:

Value	Meaning
'r'	Open existing database for reading only
'w'	Open existing database for reading and writing
'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
'n'	Always create a new, empty database, open for reading and writing
"""

import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()