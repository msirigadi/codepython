"""
After completing a task, we would like to remove it from our database. To do
this, we must use the SQL statement called DELETE:

DELETE FROM table_name WHERE condition;

Let's look at what removing the task with id = 1 might look like:

DELETE FROM tasks WHERE id = 1;

NOTE: If you forget about the WHERE clause, all data in the table will be deleted.
"""

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('DELETE FROM tasks WHERE id = ?', (1,))
conn.commit()
conn.close()