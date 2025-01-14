"""
In the csv module, there is an analogous class called DictWriter with which we
can map dictionaries to rows. Unlike the DictReader object, when creating the
DictWriter object, we must define a header. Let's look at the example in the
editor.

To create the DictWriter object, we use a file object and a list containing
column names. Note that before saving the value, we first call the writeheader
method, which adds the header to the first line of the file. After that we add
rows with values by passing dictionaries to the writerow method.
"""

import csv

with open('exported_contacts1.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-101'})


