"""
The function we’ll use for our experiments is named showinfo(), it comes from
the messagebox module, and it needs two arguments which are strings:

messagebox.showinfo(title, info)

the first string will be used by the function to title the message box which
will appear on the screen; you can use an empty string, and the box will be
untitled then;
the second string is a message to display inside the box; the string can be of
any length (but remember, the screen isn’t elastic and won’t stretch if you’re
going to display a whole encyclopedia volume); note: you can use the \n digraph
to visually break the info into separate lines.
"""

import tkinter as tk
from tkinter import messagebox

def clicked():
    messagebox.showinfo("Info", "some\ninfo")

window = tk.Tk()

button_1 = tk.Button(window, text="Show info", command=clicked)
button_1.pack()

button_2 = tk.Button(window, text="Quit", command=window.destroy)
button_2.pack()

window.mainloop()
