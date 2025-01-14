"""
create an Element object yourself. Let's see how to build an XML document
in Python.

The Element class constructor takes two arguments. The first is the name of the
tag to be created, while the second (optional) is the attribute dictionary. In
the example in the editor, we've created the root element represented by a data
tag with no attributes - look at the code.

Result:

<data />

In the example above, we use the dump method, which allows us to debug either
the whole tree or a single element.

In addition to the Element class, the xml.etree.ElementTree module offers a
function for creating child elements called SubElement. The SubElement function
takes three arguments.

The first one defines the parent element, the second one defines the tag name,
and the third (optional) defines the attributes of the element.

NOTE: To save a document using the write method, we need to have an ElementTree
object. To do this, pass our root element to its constructor:
"""

import xml.etree.ElementTree as ET

root = ET.Element('data')

movie_1 = ET.SubElement(root, 'movie', {'title': 'The little prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})

ET.dump(root)

tree = ET.ElementTree(root)
tree.write('movies1.xml', 'UTF-8', True)
