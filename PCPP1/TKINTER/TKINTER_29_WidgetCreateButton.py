"""
Each tkinter widget is created by a constructor of its class. The very first
argument of the constructor invocation is always the master widget i.e., the
widget that owns the newly created object.

widget = Widget(master, option, ... )


The master widget is just the main window in most cases, but can be also a
Frame or a LabelFrame (described in the next section).

The constructor accepts a set of arguments that configure the widget. Different
widgets use different sets of arguments.

As we mentioned before, all widgets fall into two categories: clickable and
non-clickable

Button property	    Property meaning
command	            the callback being invoked when the button is clicked
                    justify	the way in which the inner text is justified:
                    possible (self-describing) values are:
                    LEFT, CENTER, and RIGHT
state	            if you set the property to DISABLED, the button becomes
                    deaf and doesn’t react to clicks, while its title is shown
                    in gray; setting it to NORMAL restores normal button
                    functioning; when the mouse is located above the button,
                    the property changes its value to ACTIVE

Button method	    Method role
flash()	            the button flashes a few times but doesn’t change its state
invoke()	        activates the callback assigned to the widget and returns
                    the same value the callback returned; note: this is the
                    only way to invoke your own callback explicitly, as the
                    event manager must be aware of the fact
"""

import tkinter as tk
from tkinter import messagebox

def switch():
    if button_1.cget('state') == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)

def mouseover(ev):
    button_1['bg'] = 'green'

def mouseout(ev):
    button_1['bg'] = 'red'

window = tk.Tk()
button_1 = tk.Button(window, text="Enabled", bg="red")
button_1.bind("<Enter>", mouseover)
button_1.bind("<Leave>", mouseout)
button_1.pack()
button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()
window.mainloop()

