"""
the default mouse cursor reveals itself as an arrow. Sometimes, when it enters
a specific area, its shape can change (e.g., over input fields).

You have the power to order the cursor to change to a different cursor over
each of the widgets, as every widget has the property we’re talking about.
"""

import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, text="heart", cursor="heart")
label_3.pack()
window.mainloop()

