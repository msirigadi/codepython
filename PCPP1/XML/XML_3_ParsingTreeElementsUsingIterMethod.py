"""
The xml.etree.ElementTree module, or more precisely, the Element class, provides
 several useful methods for finding elements in an XML document. Let's start
 with the method called iter.

The iter method returns all elements by having the tag passed as an argument.
The element that calls it is treated as the main element from which the search
starts. In order to find all matches, the iterator iterates recursively through
all child elements and their nested elements.

Look at the code in the editor to see an example of a search for all items with
the author tag.

Result:

Antoine de Saint-Exupéry
William Shakespeare
"""


import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('books.xml')
root = tree.getroot()

for author in root.iter('author'):
    print(author.text)