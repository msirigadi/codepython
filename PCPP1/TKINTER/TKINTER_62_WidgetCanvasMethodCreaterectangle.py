"""
Drawing a rectangle can be done by the create_rectangle() method:

canvas.create_rectangle(x0,y0,x1,y1, ...,xn,yn,option...)

The method draws a rectangle specified with two opposite vertices at the
(x0,y0) and (x1,y1) points.

Some of the possible invocation options are:

Option name	    Option meaning
outline	        rectangle edge color (if specified as an empty string, the
                edge is transparent)
fill	        rectangle interior color
width	        rectangle edge width in pixels (default: 1)
"""

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.create_rectangle(200, 100, 300, 300, outline="white", fill="red", width=5)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()