"""
The most interesting create_line() options are as follows:

Option name	    Option meaning
arrow	        normally, the chain ends aren’t marked in any special way, but
                you may want them to be finished with arrowheads; setting the
                arrow option to FIRST results in drawing an arrowhead at the
                chain’s beginning, LAST at the chain’s end, BOTH at both sides
                of the chain.
fill	        chain color (setting the option to an empty string causes the
                line to be transparent)
smooth	        setting it to True rounds the chain’s corners using a set of
                connected parabolas
width	        line width (default: 1 pixel)

Let’s see them in action.

Look at the sample code we've provided in the editor. We’ve drawn the same
chain, but we’ve added some options to the create_line() invocation.
"""

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="yellow")
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380,
                   arrow=tk.BOTH, fill="red", smooth=True, width=3)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()