"""
Create database using SQLite database management system

sqlite3 – the TODO application
Have you ever forgotten to do anything during the day? If so, it's time to
finally solve this problem. Let's create a simple project called TODO, during
which we’ll create a database to store tasks (to do) along with their
priorities. The structure of our database will consist of only one table
called tasks:

Task
=====
id
name
priority

"""

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
"""
c.execute('''CREATE TABLE tasks(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
);''')
"""
c.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
);''')