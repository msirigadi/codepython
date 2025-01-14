"""
The destroy() method is very destructive. It removes the widget completely, not
only from your sight, but also from the event manager’s memory, as the widget’s
object is deleted and becomes inaccessible.

Note: if the widget you want to destroy has children (when other widgets are
embedded inside it, which can happen with frames) the children will be
destroyed, too (this rule works recursively).
"""

import tkinter as tk

def suicide():
    frame.destroy()


window = tk.Tk()
frame = tk.Frame(window, height=100, width=200, bg='green')
button = tk.Button(frame, text="I'm a frame's child")
button.place(x=10, y=10)
frame.after(5000, suicide)
frame.pack()
window.mainloop()