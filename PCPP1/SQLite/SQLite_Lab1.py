"""
Objectives
improving the student's skills in interacting with the SQLite database;
using known methods of the Cursor object.

Scenario
Our TODO application requires you to add a little security and display the
data saved in the database. Your task is to implement the following
functionalities:

1. Create a find_task method, which takes the task name as its argument.
The method should return the record found or None otherwise.

2. Block the ability to enter an empty task (the name cannot be an
empty string).
3. Block the ability to enter a task priority less than 1.
4. Use the find_task method to block the ability to enter a task with the
same name.
5. Create a method called show_tasks, responsible for displaying all tasks
saved in the database.

Test data:

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)

Example input:
Enter task name: My second task
Enter priority: 2

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)
"""

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo2.db')
        self.c = self.conn.cursor()
        self.create_tasks_table()

    def create_tasks_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                priority INTEGER NOT NULL)
        ''')

    def add_task(self):
        name = input("Enter task name: ")
        priority = int(input("Enter task priority: "))

        if len(name) == 0 or priority < 1:
            return

        if self.find_task(name) is not None:
            return

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)',
                    (name, priority))
        self.conn.commit()

    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)

    def find_task(self, name):
        for row in self.c.execute('SELECT * FROM tasks'):
             if row[1] == name:
                 return row

        return None

todo = Todo()
todo.add_task()
todo.show_tasks()
