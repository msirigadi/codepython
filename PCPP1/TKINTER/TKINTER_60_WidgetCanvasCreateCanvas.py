"""
Canvas – a widget that behaves like a... canvas. It’s a flat, rectangular
surface that you can cover with drawings, text, frames, and other widgets.
Please treat this story as a basic introduction to the Canvas facilities. It
can do much more for you – for example, it can scroll itself and react to many
events – we hope you’ll explore these issues on your own while we show you how
to start your new adventure.

This will require neither palette nor easel – Canvas brings you all you need.

Take a look at the code.

It creates a 400 x 400-pixel canvas with a yellow background. Next, it draws a
line (precisely: a polygonal chain) consisting of three line segments. The
application can be terminated using the Quit button.

First, we’ll show you how to create a canvas. This is done with a constructor
named Canvas().

c = Canvas(master, options...)


Its first argument specifies the master widget (as usual). A set of keyword
arguments specifies the properties of the canvas. The most usable of them are
as follows:

Property name	Property role
borderwidth	    canvas border’s width in pixels (default: 2)
background (bg)	canvas border’s color (default: the same as the underlying window’s color)
height	        canvas height (in pixels)
width	        canvas width (in pixels)

An existing Canvas offers a set of methods designed to create different
graphical constructs. To create a polygonal chain, you need to use the one
named create_line():

canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option...)


The method draws a line connecting the points of specified coordinates (xi,yi),
starting at (x0,y0) and ending at (xn,yn) – as you can see, each pair of
positional arguments describes one point.

If you want to draw just one segment, you need to specify four values (i.e.,
the coordinates of two points).
"""

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()