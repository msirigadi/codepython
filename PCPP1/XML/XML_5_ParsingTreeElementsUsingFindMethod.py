"""
Another useful method used to parse an XML document is a method called find.
The find method returns the first child element containing the specified tag or
matching XPath expression. Look at the code in the editor.

Result:

The Little Prince

In the example, we use the find method to find the first child element
containing the book tag, and then display the value of its title attribute.
Note that the element from which we start the search is the root element.
"""

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

print(root.find('book').get('title'))