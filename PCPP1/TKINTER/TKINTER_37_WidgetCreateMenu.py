"""
Menus

mnu = Menu(master, option, ...)

Let’s summarize the most important menu traits:

- a classic menu is actually a horizontal bar located at the top of the
application window;
- the bar contains a number of horizontally deployed options, often referred to
as items or entries;
- these options can have hot-keys (keyboard shortcuts enabling the user to
quickly access selected operations without using a mouse; usually, hot-keys are
triggered by pressing Alt-hotkey on the keyboard)
- selecting a menu’s option (it doesn’t matter whether through a hotkey or by a
mouse click) causes one of two effects:
    * it launches a callback bound to the option;
    * it unrolls a new menu (actually a submenu)
- if you want to have such a menu within your Tkinter application, you have to:
    * create a top-level menu object;
    * embed it inside the window;
    * bind a number of required submenus (this is called a cascade) or connect
    a single callback.

Our steps are as follows:

line 5: we define a simple callback which displays the About dialog;
line 9: main window creation (nothing special at all)
line 12: we create the main menu object...
line 13: and embed it into the main window (note the way in which the config()
method is used and which property we utilize to bind the menu)
line 16: we create a submenu object (note the master window argument
specification)
line 17: we add the submenu to the main menu’s first item (note the
add_cascade() method invocation)
line 20: we create another submenu object…
line 21: ...and bind a callback to it (note the add_command() method invocation)

Run the code and test it. Do you see that strange dashed line visible when you
click the File main menu item?

Don’t worry, this it’s normal. We’ll deal with it soon.

A menu like this has one important disadvantage – it’s hard to use it without a
mouse. Of course, you can use the Alt key to activate the menu and navigate
through it using the cursor keys and Enter (you can test this), but we need
something quicker and more convenient.
"""

import tkinter as tk
from tkinter import messagebox

def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

window = tk.Tk()

# main menu creation
main_menu = tk.Menu(window)
window.config(menu=main_menu)

# 1st main menu item: an empty (as far) submenu
sub_menu_file = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=sub_menu_file)

# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app)

window.mainloop()