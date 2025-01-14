"""
The LabelFrame widget is a Frame enriched with a visible border and a title
(also visible). The title may be located at one of 12 possible places on the
border line.

lfrm = LabelFrame(master, option, ...)

Some of the usable LabelFrame properties are gathered here:

LabelFrame property	Property meaning
takefocus	        the same as for the Frame
text	            the LabelFrame’s title
labelanchor	        the title’s location, defined as a string containing a
                    quasi-compass coordinate (as shown by the image)

                    ---nw----------n--------ne---
                    |                           |
                    wn                          en
                    |                           |
                    w                           e
                    |                           |
                    ws                          es
                    |                           |
                    ---sw---------s---------se---
"""

import tkinter as tk

window = tk.Tk()
label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                                width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2", labelanchor="se",
                                width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=40)
button_2_1.grid(row=0, column=0)
button_2_2.grid(row=1, column=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()