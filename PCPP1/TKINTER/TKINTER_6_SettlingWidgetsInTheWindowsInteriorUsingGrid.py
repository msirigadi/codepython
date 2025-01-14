"""
The grid geometry manager is in the middle, in between the other two geometry
managers. It gives you a chance to express your general wishes and tries to
deploy the widgets according to them. Note the word general – they aren't as
precise as the ones used by place, but are far more detailed than those
utilized by pack.

grid() sees the window's area as a... grid. This means that the whole of the
window's interior is divided into a number of columns of equal width and a
number of rows of equal height.

The grid itself is not visible – the distribution is modeled inside the
manager and you are only able to know its effects i.e., the widget's final
arrangement.

You're not obliged to declare the number of rows and columns in
advance – grid() finds the proper numbers for you.

The most commonly used grid() method parameters are gathered below (as,
previously, all of them are passed as keyword arguments):

column=c – deploys the widget in the column number c; note: the columns'
numbers start from zero, and if you omit this argument, the manager will
assume 0 (the left-most column)
row=r – deploys the widget in the row number r; if you omit this argument,
the manager will assume the first free row starting from the top;
columnspan=cs – determines how many neighboring columns the widget occupies;
the parameter defaults to 1 (the widget won't cross a single grid's cell)
rowspan=rs – works as columnspan but refers to rows.
"""

import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text='Button #1')
button2 = tk.Button(window, text='Button #2')
button3 = tk.Button(window, text='Button #3')

# Example 1
# The window is divided into nine cells: three rows and three columns. The
# buttons are settled on the grid's diagonal.
#button1.grid(row=0, column=0)
#button2.grid(row=1, column=1)
#button3.grid(row=2, column=2)

# Example2
# the manager noticed that the total number of columns is actually two, not
# three as in the previous code. This is why the window looks different.
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)
button3.grid(row=2, column=0, columnspan=2)

window.mainloop()
