"""
If you want to modify a property named prop, existing within a widget named
wid, and you’re going set its value to val, you can use the config() method,
just like here:

wid.config(prop=val)

This means that if you want to unbind your current callback from a Button named
b1, you would use an invocation like this one:

b1.config(command=lambda:None)

This binds an empty (i.e., doing absolutely nothing) function to the widget’s
callback.
"""

import tkinter as tk
from tkinter import messagebox

def on_off():
    global switch

    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")

    switch = not switch

def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")

switch = True
window = tk.Tk()
button_1 = tk.Button(window, text='On/Off', command=on_off)
button_1.pack()
button_2 = tk.Button(window, text='Peekaboo!', command=peekaboo)
button_2.pack()
window.mainloop()