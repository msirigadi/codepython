"""
If your widget is a clickable one, you can connect a callback to it using its
command property, while the property can be initially set by the constructor
invocation.

We’ve already practiced this, so the snippet in the editor won’t be a surprise
to you.

Note – there are three widgets in all, but only one of them (the Button) is
clickable by nature. Such a widget’s constructor is equipped with the command
parameter, which is used to bind a callback.
"""

import tkinter as tk
from tkinter import messagebox

def click():
    messagebox.showinfo("Clicks!", "I love\nclicks")

window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#09A1AA")
frame.pack()

window.mainloop()