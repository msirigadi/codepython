"""
The second method relies on two specialized widget methods, the first named
cget() designed to read the property’s value, and the second named config(),
which allows you to set a new value to the property.

This is what they look like:

old_val = Widget.cget("prop")

Widget.config(prop=new_val)
"""

import tkinter as tk

def on_off():
    global button
    state = button.cget('text')
    if state == "ON":
        state = "OFF"
    elif state == "OFF":
        state = "ON"

    button.config(text=state)

window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()