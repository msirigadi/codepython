"""
Saving data to a CSV file is done using the writer object provided by the
csv module. To create it, we need to use a function called writer, which takes
the same set of arguments as the reader function.

We first open the file for writing. The 'w' mode creates a file for us if it
hasn't already been created. Next, we create a writer object that we use to
add rows using the writerow method. The writerow method takes a list of values
as an argument, and then saves them as one line in a CSV file.
"""

import csv

with open('exported_contacts.csv', 'w', newline='') as csvfile:
    #writer = csv.writer(csvfile, delimiter=',')

    #writer.writerow(['Names', 'Phones'])
    #writer.writerow(['mother', '222-555-101'])
    #writer.writerow(['father', '222-555-102'])
    #writer.writerow(['wife', '222-555-103'])
    #writer.writerow(['mother-in-law', '222-555-104'])


    """
    Another Solution below
    =======================
    Imagine a situation where you add a contact containing the separator used 
    to separate the values in the CSV file. By default, these values are 
    quoted, but you can change this with the quotechar argument, which must be 
    a single character.
    
    The last argument called quoting, specifies what values should be quoted. 
    The default value QUOTE_MINIMAL means that only values with special 
    characters such as separator or quotechar will be quoted. In our case, 
    it's the value of "grandmother, grandfather and auntie".
    """

    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['Names', 'Phones'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105'])
