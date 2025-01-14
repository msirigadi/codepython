"""
closing the window without asking the user if they are really sure that this is
exactly what they want to do isn't a good way to build up a relationship with
them.

We definitely want to ask the user before we permanently remove their window
from sight.

Fortunately, tkinter is very helpful with this issue. There is a module named
messagebox (the name speaks for itself) which is your great companion in this
and similar matters.

messagebox is able to create dialog boxes intended to ask questions, display
messages, and to receive a user's reply.

The dialog box is an example of a modal window – a window which grabs the whole
of the application's focus. It means that all other application widgets become
deaf as long as the modal window is present.
"""

import tkinter
from tkinter import messagebox

def Click():
    reply = messagebox.askquestion('Quit?', 'Are you sure?')
    if reply == 'yes':
        skylight.destroy()

skylight = tkinter.Tk()
skylight.title('Skylight')

button = tkinter.Button(skylight, text='Bye', command=Click)
button.place(x=10, y=10)
skylight.mainloop()