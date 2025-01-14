"""
A widget's property is not just an object property. Although every widget is
actually an object, you can access its properties by using the dot notation.
You have to use one of two possible ways of reading and setting widget
properties’ values.

The first method is based on using a dictionary which exists inside every
widget. Assuming that a widget named Widget has a property named prop and you
want to read its value and then set it with a new value, you can do this in the
following way:

old_val = Widget["prop"]

Widget["prop"] = new_val
"""

import tkinter as tk

def on_off():
    global button
    state = button['text']
    if state == "ON":
        state = "OFF"
    elif state == "OFF":
        state = "ON"

    button['text'] = state

window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()