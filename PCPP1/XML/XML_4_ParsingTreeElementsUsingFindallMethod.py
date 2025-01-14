"""
The Element object has a method called findall to search for direct child
elements. Unlike the iter method, the findall method only searches the children
at the first nesting level. Take a look at the example in the editor.

The example doesn't return any results, because the findall method can only
iterate over the book elements that are the closest children of the root
element. The correct code looks like this:

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for book in root.findall('book'):
    print(book.get('title'))

Result:

The Little Prince
Hamlet
"""

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for author in root.findall('author'):
    print(author.text)


for book in root.findall('book'):
    print(book.get('title'))