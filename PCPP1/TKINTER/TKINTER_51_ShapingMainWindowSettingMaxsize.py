"""
There’s also a method called maxsize(), which protects the window from becoming
too large.
"""

import tkinter as tk

window = tk.Tk()
window.maxsize(width=500, height=300)
window.geometry("200x200")
window.mainloop()