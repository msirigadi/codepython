"""
A button visible on the screen is, in fact, a reflection of an object of the
Button class. To bring a button to life, you have to:

create a Button class object (it'll be done by the class's constructor)
place the button inside the main window (it'll be done by one of the window's
methods)
Note the distinction: it can be said that the button creates itself, but to
make it visible, you need the window's (not the button's!) method.
"""

import tkinter

skylight = tkinter.Tk()
skylight.title('Skylight')

button = tkinter.Button(skylight, text='Bye')
button.place(x=10, y=10)

skylight.mainloop()