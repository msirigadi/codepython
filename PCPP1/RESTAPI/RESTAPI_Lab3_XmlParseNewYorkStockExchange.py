"""
Objectives
Learn how to:

- read and parse simple XML files using the xml.etree.ElementTree module;
- deal with XML nodes and properties.

Scenario
Download and open the following XML file in your favorite text editor:

nyse.xml

It's a small excerpt of the New York Stock Exchange quotes list. Take a
look at it and analyze its structure. You need to do this as your task is
to write a code which reads the data and presents it in a form similar
to this one:

z:/>python 03.py
COMPANY			LAST		CHANGE		MIN	        MAX
------------------------------------------------------------
IBM Co			159.696		-0.384		161.255	    159.38
.
.
.


Hints:

1. don't forget to handle at least two possible exceptions: FileNotFoundError
and xml.etree.ElementTree.ParseError;
2. feel free to improve and beautify the output — we know perfectly well that
ours is not very sophisticated and rather ugly.

"""
import xml.etree.ElementTree

key_names = ["COMPANY", "LAST", "CHANGE", "MIN", "MAX"]
key_width = [40, 10, 10, 10, 10]

def show_header():
    for (n, w) in zip(key_names, key_width):
        print(n.ljust(w), end = "")
    print()

    for w in key_width:
        print('_' * w, end = "")
    print()

def show_prop(prop):
    for (n, w) in zip(key_names, key_width):
        n = n.lower()
        if n == "company":
            print(prop.text.ljust(w), end = "")
            continue
        print(prop.attrib[n].ljust(w), end = "")
    print()


try:
    tree = xml.etree.ElementTree.parse("C:\\Users\\msiri\\Json_Files\\nyse.xml")
except FileNotFoundError:
    print("Stock data file not found")
    exit(1)
except xml.etree.ElementTree.ParseError:
    print("Stock data file contains invalid data")
    exit(2)

data = tree.getroot()
show_header()
for prop in data:
    if prop.tag == "quote":
        show_prop(prop)



"""
Alternative solution
-------------------- 

import xml.etree.ElementTree

try:
    NYSE = xml.etree.ElementTree.parse('nyse.xml')
except FileNotFoundError:
    print("Stock data file not found")
    exit(1)
except xml.etree.ElementTree.ParseError:
    print("Stock data file contains invalid data")
    exit(2)
quotes = NYSE.getroot()
print('COMPANY'.ljust(40), end='')
print('LAST'.ljust(10), end='')
print('CHANGE'.ljust(10), end='')
print('MIN'.ljust(10), end='')
print('MAX'.ljust(10), end='')
print()
print('-' * 80)
for quote in quotes.findall('quote'):
    print(quote.text.ljust(40), end='')
    print(quote.attrib['last'].ljust(10), end='')
    print(quote.attrib['change'].ljust(10), end='')
    print(quote.attrib['min'].ljust(10), end='')
    print(quote.attrib['max'].ljust(10), end='')
    print()
"""