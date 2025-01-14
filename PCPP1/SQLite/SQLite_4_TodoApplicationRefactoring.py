"""
You've probably noticed that adding new functionalities to our TODO application
would be very difficult. This is a sign that our application requires
refactoring. Below are suggestions for changes we can make:

creating a class called TODO that will connect to the database in the
constructor. If you want, you can implement a separate method called connect
for this purpose;

moving the code responsible for creating the tasks table to the method named
create_tasks_table;
creating a method called add_task that will get the task name and priority from
the user instead of using hardcoded values.
"""

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("todo1.db")
        self.c = self.conn.cursor()
        self.create_tasks_table()

    def create_tasks_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                priority INTEGER NOT NULL
            )
        ''')

    def add_task(self):
        name = input("Enter task name: ")
        priority = int(input("Enter priority: "))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)',
                       (name, priority))
        self.conn.commit()
        self.conn.close()

todo = Todo()
todo.add_task()

