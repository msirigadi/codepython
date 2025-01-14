"""
Place is the most detailed one. It forces you to precisely declare a widget's
location, pixel by pixel. It won't, however, protect you from some common
mistakes causing the widgets to overlap each other or to place some of them,
partially or fully, outside the window.

The place geometry manager demands the usage of the place() method. Note: the
method is invoked from within the widget's object, not the window, as the
widget is always aware of the window it belongs to (it gets the information
from the constructor's very first argument).

The most usable place() method parameters are as follows (all of them are
passed as keyword arguments):

height=h – the widget's desired height measured in pixels; if the parameter is
omitted, the widget's height will be determined automatically;
width=w – the widget's desired width measured in pixels; if the parameter is
omitted, the widget's width will be determined automatically;
x=x – the widget's top-left pixel's horizontal coordinate measured relative to
the home window's top-left corner;
y=y – the widget's top-left pixel's vertical coordinate measured relative to
the home window's top-left corner.

Also play with height and width
"""

import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text='Button #1')
button2 = tk.Button(window, text='Button #2')
button3 = tk.Button(window, text='Button #3')

#button1.place(x=10, y=10)
#button2.place(x=20, y=40)
#button3.place(x=30, y=70)

# Change width and height
button1.place(x=10, y=10, width=150)
button2.place(x=20, y=40)
button3.place(x=30, y=70, height=50)

window.mainloop()