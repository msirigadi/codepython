"""
The Checkbutton is a two-state switch that can be ticked (checked) or not;
thus, it is a handy tool to represent yes/no user choices.


Let's start with its properties:

Checkbutton property	Property meaning
bd	                    the checkbutton frame width (default is two pixels)
command	                the callback being invoked when the checkbutton changes
                        its state
justify	                the same as for Button
state	                the same as for Button
variable	            an observable IntVar variable reflecting the widget’s
                        state; defaultly it’s set to 1 when the checkbutton is
                        checked, and to 0 otherwise
offvalue	            the non-default value being assigned to a variable when
                        the checkbutton is not checked
onvalue	                the non-default value being assigned to a variable when
                        the checkbutton is checked

And now some of its methods:

Checkbutton method	Method role
deselect()	        unchecks the widget
flash()	            the same as for Button
invoke()	        the same as for Button
select()	        checks the widget
toggle()	        toggles the widget (changes its state to the opposite one)

The sample we’ve prepared for you makes use of the checkbutton and does
two things:

counts all the checkbutton’s state changes and stores the result in
cnt variable;
presents the current cnt value and the checkbutton’s state after clicking the
Show button.
"""

import tkinter as tk
from tkinter import messagebox

def show():
    messagebox.showinfo("", "counter=" + str(counter) + ",state=" + str(switch.get()))

def count():
    global counter
    counter += 1

window = tk.Tk()
switch = tk.IntVar()
counter = 0
button = tk.Button(window, text="show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()
window.mainloop()





