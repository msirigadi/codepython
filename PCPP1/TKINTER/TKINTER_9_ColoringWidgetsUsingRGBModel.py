"""
The third method you can use is based on the fact that each color can be
obtained by mixing (adding) three primary colors: red (R), green (G) and
blue (B). The phenomenon is utilized by the so-called RGB color model which is
one of the additive color models and it's widely used in many application,
e.g. in color displays of different kinds.

One of the RGB model implementations allows you to set the saturation of every
of primary colors in the range <0..255> what gives 256 different saturation
levels, from color's absence (saturation 0) to full color's presence
(saturation 255).

Specify all these (more than 16 million) mixes in a comprehensive way

It's is done by a trick used extensively in web pages – as a string starting
with a hash (#) followed by 6 hexadecimal digits. Each pair of the digits forms
the value from range 0x00..0xFF (0..255) what determines the specific component
level.

This is how it works:

#RRGGBB

All three pairs (RR, GG and GG) are two-digit hexadecimal number so:

#000000 is black
#FFFFFF is white
#FF0000 is red
#00FF00 is green
#0000FF is blue
#00FFFF is turquoise
#FF00FF is violet
"""

import tkinter as tk

window = tk.Tk()

button = tk.Button(window, text='Button #1',
                   bg='#FF7F50',
                   fg='#BDB76B',
                   activebackground='#8968CD',
                   activeforeground='#FFFACD')
button.pack()
window.mainloop()