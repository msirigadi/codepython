"""
Reading data saved in the database is done with the well-known Cursor object.
After calling the execute method with the appropriate SELECT statement, the
Cursor object is treated as an iterator. Look at the code in the editor.
"""

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Solution 1
for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()


"""
# Solution 2

If you don't want to treat the Cursor object as an iterator, you can use its 
method called fetchall. The fetchall method fetches all records (those not yet 
fetched from the query result)


The fetchall method is less efficient than the iterator, because it reads all 
records into the memory and then returns a list of tuples. For small amounts of 
data, it doesn't matter, but if your table contains a huge number of records, 
this can cause memory issues.

NOTE: The fetchall method returns an empty list when no rows are available.
"""

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('SELECT * from tasks')
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()


"""
In addition to the iterator and the fetchall method, the Cursor object provides 
a very useful method called fetchone to retrieve the next available record. 
Look at the code in the editor.
The fetchone method returns None if there is no data to read.
"""

conn = sqlite3.connect('todo1.db')
c = conn.cursor()

c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()