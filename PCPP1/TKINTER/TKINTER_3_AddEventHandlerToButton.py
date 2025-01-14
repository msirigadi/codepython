"""
An event handler is a piece of code responsible for responding to all clicks
addressed to our button.

The event handler we need has a simple assignment – we want it to just
terminate our application. This crucial operation is done with a main window
method called – don't be afraid – destroy(). It's a parameterless method,
as destroying needs (in contrast to creation) no arguments at all.

How do we write the event handler?

It's a function. Just a simple function. The handler used by the button has to
be a parameterless function of any name. Don't forget that the function will
be invoked, not by us, but only by the controller.

Furthermore, invoking your own handler is strictly prohibited, as it can
completely confuse the event controller.

Note: a function designed to be invoked by someone/something else (not us!) is
often called a callback.
"""

import tkinter

def Click():
    skylight.destroy()

skylight = tkinter.Tk()
skylight.title('Skylight')

button = tkinter.Button(skylight, text='Bye', command=Click)
button.place(x=10, y=10)

skylight.mainloop()

