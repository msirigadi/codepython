"""
An event object is an instantiation of the Event class. Actually, it’s a
container filled with some more or less helpful data. The data describe all the
circumstances which are accompanied within the event, and it is dispatched to a
number of the object’s properties.

class Event:
    :
    :

Note: not all properties have meaning for every event. If the event is related
to some of the mouse actions, the object’s parts referring to the keyboard
remain uninitialized, and vice versa.

Property name	Property role
widget	        The widget’s object (not the widget’s name!) to which the event
                is addressed
<x>
<y>	            The mouse cursor’s coordinates at the moment of the event’s
                occurrence (both coordinates are counted relative to the
                target widget)
<x_root>
<y_root>	    As above, but relative to the screen
    .
    .
    .
"""

import tkinter as tk
from tkinter import messagebox

def click(event=None):
    if event is None:
        messagebox.showinfo("Click!", "I love clicks")
    else:
        string = "Widget = " + str(event.widget) + \
                ", x = " + str(event.x) + \
                ", y = " + str(event.y) + \
                ", num = " + str(event.num) + \
                ", type = " + event.type
        print(string)
        messagebox.showinfo("Clicks!", string)

window = tk.Tk()

label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#0000FF")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()

