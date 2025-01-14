"""
The askretrycancel() function creates a dialog containing a warning sign
instead of a question mark and two buttons titled Retry and Cancel (it returns
True for Retry and False otherwise).
"""

import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askretrycancel("?", "Oops, I failed again!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
