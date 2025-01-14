"""
In addition to iterating over tree elements, we can access them directly using
indexes
"""

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for book in root:
    print(book.tag, book.attrib)
    print(book[0].tag, book[0].text)
    print(book[1].tag, book[1].text, '\n')