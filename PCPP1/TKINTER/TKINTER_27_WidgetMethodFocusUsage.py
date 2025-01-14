"""
widgets may or may not have the focus. At most one widget can have the focus.
When you use a keyboard to interact with the application, you can use the Tab
and Shift-Tab keys to move the focus forward and backward, but the focus can
be controlled programmatically, too. There are two methods to help you cope
with this issue. Assuming that Wi is an existing widget, the methods look
as follows:

wi.focus_get()
wi.focus_set()


the focus_get() method returns a reference to the currently focused widget, or
None when no widget owns the focus (note: you can invoke the method from any
widget, including the main window)

the focus_set() method focuses the widget from the method which was invoked,
so you have to choose it carefully.
"""

import tkinter as tk

def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()

    window.after(1000, flip_focus)

window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)
window.mainloop()