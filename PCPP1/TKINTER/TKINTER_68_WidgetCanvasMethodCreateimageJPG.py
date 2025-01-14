"""
To use a JPEG bitmap, some additional steps are required – you need to:

- import the Image and ImageTk classes from the PIL (Python Image Library)
module;
- build an object of the Image() class and use its open() method to fetch the
bitmap from the file (the argument should specify the file’s path)
- convert this object into a PhotoImage class object using an ImageTk function
of the same name;
- continue as usual.
"""

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=1000, bg="black")
jpg = Image.open('Atharv.JPG')
#width, height = jpg.size
#jpg = jpg.resize((width//2, height//2))
#jpg = jpg.rotate(180)
image = ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
canvas.grid(row=1)
window.mainloop()