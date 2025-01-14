"""
widget can be colorized. There are more options than you may suspect:

Widget property name	Property role
background
bg	                    The color of the widget’s background (you can freely
                        use either of these two forms)
foreground
fg	                    The color of the widget’s foreground (note: it can
                        mean different things in different widgets; in general,
                        it’s used to specify text color)
activeforeground
activebackground	    Like bg and fg but used when the widget becomes active

disabledforeground	    The width of the widget
"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button")
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg="#000000")
button_2.config(fg="yellow")
button_2.config(activebackground="#FF0000")
button_2.config(activeforeground="green")
window.mainloop()