    """
Objectives
improving the student's skills in interacting with the SQLite database;
using known SQL statements.

Scenario
The application is almost ready. Let's add the missing functionalities to it:

1. Create a method called change_priority, responsible for updating task
priority. The method should get the id of the task from the user and its new
priority (greater than or equal to 1).
2. Create a method called delete_task, responsible for deleting single tasks.
The method should get the task id from the user.
3. Implement a simple menu consisting of the following options:

1. Show Tasks
2. Add Task
3. Change Priority
4. Delete Task
5. Exit

where:

Show Tasks (calls the show_tasks method)
Add Task (calls the add_task method)
Change Priority (calls the change_priority method)
Delete Task (calls the delete_task method)
Exit (interrupts program execution)

The program should obtain one of these options from the user, and then call
the appropriate method of the TODO object. Choosing option 5 must terminate
the program. A menu should be displayed in an infinite loop so that the user
can choose an option multiple times.

"""

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo3.db')
        self.c = self.conn.cursor()
        self.create_table()
        self.menu()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            priority INTEGER NOT NULL)
        ''')

    def menu(self):
        while True:
            print("""
                    1. Show Tasks
                    2. Add Task
                    3. Change Priority
                    4. Delete Task
                    5. Exit""")

            choice = int(input("Enter you choice: "))
            if choice not in [1, 2, 3, 4, 5]:
                print("Not a valid choice")
                continue

            if choice == 1:
                self.show_tasks()
            elif choice == 2:
                self.add_task()
            elif choice == 3:
                self.change_priority()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                exit()

    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)

    def add_task(self):
        name = input("Enter task name: ")
        priority = int(input("Enter task priority: "))

        if len(name) == 0 or priority < 1:
            return

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)',
                       (name, priority))
        self.conn.commit()

    def change_priority(self):
        id = int(input("Enter id of the task: "))
        priority = int(input("Enter new priority: "))

        self.c.execute('UPDATE tasks SET priority=? WHERE id=?',
                       (priority, id))
        self.conn.commit()

    def delete_task(self):
        id = int(input("Enter id of the task to be deleted: "))

        self.c.execute('DELETE FROM tasks WHERE id=?', (id,))
        self.conn.commit()

todo = Todo()