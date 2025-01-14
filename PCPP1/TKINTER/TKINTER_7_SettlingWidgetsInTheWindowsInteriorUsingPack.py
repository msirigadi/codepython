"""
If you don't want to deploy the widgets manually and worry about possible
conflicts and failures, you may entrust the whole problem to tkinter. It'll try
to guess your intentions and to find the best location for each widget.
Unfortunately, its assumptions may not live up to your expectations, and the
final result can be really disappointing. This method of settling widgets is
implemented by the pack geometry manager.

The third, fully automatic geometry manager is named pack() as it packs
subsequent widgets into the window's interior. This means that the order in
which the widgets are packed matters – in contrast to grid() and place().

The default pack's operation tends to deploy all subsequent widgets in one
column, one below the other. You can change this behavior to a limited extent
by using the following parameters:

side=s – forces the manager to pack the widgets in a specified direction, where
s can be specified as:

TOP – the widget is packed toward the window's top (it's manager's default behavior)
BOTTOM – the widget is packed toward the window's bottom;
LEFT – toward the window's left boundary;
RIGHT – toward the window's right boundary;

fill=f – suggests to the manager how to expand the widget if you want it to
occupy more space than the default, while f should be specified as:

NONE – do not expand the widget (default behavior)
X – expand it in the horizontal direction;
Y – expand it in the vertical direction;
BOTH – expand it in both directions;

We want to warn you that the results produced by pack() can be extremely
surprising, and you should spend some time on your own experimenting with all
its vices.

We suggest you use it only as a temporary solution to help you get a working
application quickly, but if you want your application to look nice and to be
legible and clear (of course, you would want that!) you'd better forget about
pack() and use either grid() (in simpler cases) or place().
"""

import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text='Button #1')
button2 = tk.Button(window, text='Button #2')
button3 = tk.Button(window, text='Button #3')

# Example 1
#button1.pack()
#button2.pack()
#button3.pack()

# Example 2
# We've ordered pack() to push the button_1 button to the right window's
# boundary.
#button1.pack(side=tk.RIGHT)
#button2.pack(side=tk.BOTTOM)
#button3.pack(side=tk.TOP)

# Example 3
# we want the button_1 button to be filled (expanded) in the vertical direction
button1.pack(side=tk.RIGHT, fill=tk.Y)
button2.pack(side=tk.BOTTOM)
button3.pack(side=tk.TOP)

window.mainloop()