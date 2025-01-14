"""
Insert values into the database created using sqlite3
"""

import sqlite3
conn = sqlite3.connect('todo.db')
c = conn.cursor()
#c.execute('INSERT INTO tasks (id, name, priority) VALUES (1, "My first task", 1);')
#conn.commit()
#c.execute('INSERT INTO tasks (id, name, priority) VALUES (?,?,?)',
#          (2, 'My second task', 2))
#conn.commit()
c.execute('INSERT into tasks (name, priority) VALUES(?,?)', ('My first task', 1))
conn.commit()
conn.close()