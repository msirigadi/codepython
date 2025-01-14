"""
To unbind a callback previously bound with the bind() method invocation, you
need to use the unbind() method:

widget.unbind(event)

The method requires one argument identifying the event being unbound.

Note: the information about a previously used callback is lost. You cannot
retrieve it automatically and you must repeat the bind() invocation.
"""

import tkinter as tk

def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>")
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch


def rhyme(event):
    global words, word_no
    word_no += 1
    label.config(text=words[word_no % len(words)])

words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0

switch = True
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off)
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1> ", rhyme)
label.pack()
window.mainloop()