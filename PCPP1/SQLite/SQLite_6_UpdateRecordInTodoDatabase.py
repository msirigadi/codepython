"""
The UPDATE statement is used to modify existing records in the database
"""

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
conn.commit()
conn.close()