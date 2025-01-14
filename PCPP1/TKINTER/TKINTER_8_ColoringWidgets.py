"""
Add colors to your widgets

the two new arguments we use in the constructor invocation: bg (what is a short
form of “background-color”) and fg (“foreground-color”). We went along the line
of least resistance here – we've just made use of regular English names of
colors and packed them inside strings.

The colors of the lowered (pressed) button are gray still. Why?

Because fb and bg refer to raised buttons only. There two additional parameters
describing the second set of colors named activeforeground and activebackground
respectively used by the event controller when the button is pressed
"""

import tkinter as tk

window = tk.Tk()

# The colors of the lowered (pressed) button are gray still
#button = tk.Button(window, text="Button #1", bg="red", fg="purple")

# second set of colors named activeforeground and activebackground when button
# is pressed
button = tk.Button(window, text="Button #1", bg="Coral", fg="dark khaki",
                   activebackground="MediumPurple3",
                   activeforeground="lemon chiffon")
button.pack()

window.mainloop()