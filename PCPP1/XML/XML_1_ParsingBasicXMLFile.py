"""
Parse books.xml
"""

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

print("Root element: ", root.tag)

for child in root:
    #print("Child element: ", child.tag)
    #print("Child attributes: ", child.attrib)
    print(child.tag, child.attrib)
    for sub_elem in child:
        print(sub_elem.tag, sub_elem.text)