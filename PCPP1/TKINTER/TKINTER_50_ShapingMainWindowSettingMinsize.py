"""
you can usually change the main window’s size on your own by dragging the
window’s bottom-right corner.

If you want your window not to be less than a desired value, you can use the
method named minsize(), with two possible arguments (you can use either of
them, or both) with self-describing names: width and height.
"""

import tkinter as tk

window = tk.Tk()
window.minsize(width=250, height=400)
window.geometry("500x500")
window.mainloop()