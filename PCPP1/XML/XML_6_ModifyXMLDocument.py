"""
Modify the element tree and create a new XML file based on it with the
following movie data:

<?xml version="1.0"?>
<data>
    <movie title="The Little Prince" rate="5"></movie>
    <movie title="Hamlet" rate="5"></movie>
</data>

To change the tag of the Element object, we must assign a new value to its
tag property
"""

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for child in root:
    child.tag = 'movie'

    # Remove author and year which are irrelevant to movies
    child.remove(child.find('author'))
    child.remove(child.find('year'))

    # Add rate as attribute to movie
    # method set allows to set new attributes
    child.set('rate', '5')

    print(child.tag, child.attrib)

    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('movies.xml', 'utf-8', True)
