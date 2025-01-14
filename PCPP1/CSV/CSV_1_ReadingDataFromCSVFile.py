"""
The Python Standard Library offers a module called csv that provides functions
for reading and writing data in CSV format. Reading data is done using the
reader object, while writing is done using the writer object. First, we'll
take a closer look at reading data using the reader object.

The reader function returns an object that allows you to iterate over each
line in the CSV file. To create it, we need to pass a file object to the reader
function. For this purpose, we can use a built-in function called open.

Note that a single line is returned as a list of strings. However, more
readable results can be obtained, e.g., by using the join method.

NOTE: The newline='' argument added to the open function protects us from
incorrect interpretation of the newline character on different platforms.
"""

import csv

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
        print(','.join(row))


"""
The csv module provides a more convenient way to read data, in which each line 
is mapped to an OrderedDict object. To achieve this, we must use the 
DictReader class in the way we show in the editor.
"""

print("*****  Solution *****")
with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], ':', row['Phone'])


"""
Like the reader function, the DictReader class accepts a file object as an 
argument. It treats the first line of the file as a header from which to read 
the keys. If your file doesn't have a header, you must define it using the 
fieldnames argument. Look at the code in the editor.

NOTE: If you define more column names than the values in the file, the missing 
values will be None.
"""

print("*****  Solution *****")
with open('contacts.csv', newline='') as csvfile:
    fieldnames = ['Names', 'Phone']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row['Names'], row['Phone'])