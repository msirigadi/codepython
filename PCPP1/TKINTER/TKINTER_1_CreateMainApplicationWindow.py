"""
The main application window (which is often the only window being used by the
application) is created by the tkinter method named Tk(). In its most commonly
used form, it needs no arguments. The object returned by the method is complete,
 but at the same time, completely invisible. Moreover, it won't be visible
 until the event controller starts.

To start the controller, you have to invoke the main window's method, named
mainloop().

Each window (including the main one) has a method named – of course – title().
The method can be invoked more than once in any moment of the window's life.

"""

import tkinter

skylight = tkinter.Tk()

# Give title name to window
skylight.title('Skylight')
skylight.mainloop()
