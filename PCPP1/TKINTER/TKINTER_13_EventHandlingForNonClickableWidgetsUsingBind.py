"""
Some of the widgets (especially those that are not clickable by nature) have
neither a command property nor a constructor parameter of that name.

Fortunately, you’re still able to bind a callback to any of the events it may
receive (including clicks, of course) and this is done with a method named – it
couldn’t be anything else – bind():

widget.bind(event, callback)

The bind() method needs two arguments:

the event you want to launch your callback with;
the callback itself.

Note:

a callback designed for usage with the command property/parameter is a
parameterless function;
a callback intended to cooperate with the bind() method is a one-parameter
function (the callback’s argument carries some info about the captured event)
fortunately, it doesn’t mean that you have to define two different callbacks
for those two applications, and this is how we’ll cope with the above requirements:

def callback(ev=None):
    :
    :

the callback will work flawlessly in both of these contexts, and moreover,
it’ll give you the chance to identify which one of the two possible styles of
launch has just occurred.

The bind remains active to the end of the application’s work, but you can also
manually unbind the event at any moment (and bind it again when you wish).
"""

import tkinter as tk
from tkinter import messagebox


def click(ev=None):
    messagebox.showinfo("Clicks!", "I love clicks")

window = tk.Tk()

label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#A123EF")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()

