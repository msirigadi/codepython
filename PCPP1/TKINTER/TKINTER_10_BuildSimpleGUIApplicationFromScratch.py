"""
Our fabulous goal will look like the vision presented below:

The GUI application should look like something in the file
'SimpleGUIApplication.png'

Our new friend is called Label – a non-clickable widget able to present short
textual information, passed to the widget's constructor using a text argument.
The text can later be changed at any moment of the widget's life.

As you can see, we're using the pack() geometry manager to compose the window.

A Frame is another non-clickable component used to group widgets and to
separate them (visually) from other window components. Our Frame plays a less
important role – it just occupies a rectangle and fills it with its own color.
We expect nothing more for now.

Our Button will be completely mute, as we haven’t bound anything to its
command property.

Our next component is completely invisible. You won't find it in the window
area.

It's the switch variable. Can't you see it? It's set to hold an object of the
IntVar class. This object is designed to store integer values. "Okay," you may
say, "can't we use a regular variable instead?"

No, we can't. Objects of the IntVar class are used by tkinter to organize
internal communication between different widgets. A regular variable can't play
such a role.

If you want such an object to store an integer value, you can't use the
assignment operator. The class offers a dedicated method for that purpose, and
the method is named set().

Note: we've used the method to store a value of 1 inside the object.

The next step adds a brand new widget to our window – it’s a Checkbutton.

It’s a small square which can be filled with a tick mark, or which can be empty.


The Checkbutton is primarily used to represent two-state selections. In other
words, it can be in one of two possible states:

the ON state when the Checkbutton is checked/ticked (which can be equated with
an affirmative answer to some question)
the OFF state when the Checkbutton is cleared (you can think of it as a kind of
negative answer)

a variable argument. Note – it’s set to the previously created switch object.
The assignment creates a bidirectional link between the object and the widget.
How does it work?

If you check or uncheck the Checkbutton, the switch object will immediately
change its state – it will keep 0 if the widget is unchecked, and 1 otherwise.

If you change the state of the switch object, the Checkbutton will immediately
reflect the change – it means that you don’t need to access the Checkbutton
itself to check/uncheck it, as you can modify the switch value instead.

Look, the switch is initially set to 1. this means that the Checkbutton will be
checked when it appears on the screen.

Now we add a very important, and internally an extremely complicated, widget,
named Entry. Look at the code in the editor.

Entry is designed to let the user enter simple, one-line data, like single
numbers, names, addresses, etc.

There are the Radiobuttons, small circles filled with a dot, or not. The most
important difference between Check- and Radiobuttons lies in the fact that
Checkbuttons are solitary (they work individually) while Radiobuttons always
work in groups and – note it! – only one of the widgets inside the group can be
checked. Clicking an unchecked member of the group will cause the currently
checked Radiobutton to change its state.

How do we achieve such an effect? The switch object will help us with it.

Our two Radiobutton constructors use two additional arguments. What roles do
they play?

The variable argument binds a switch object to both of the widgets, and this is
the clue – the fact that both Radiobuttons are bound to the same object creates
the group. Don’t forget that!
The value argument distinguishes the Radiobuttons inside the group, and thus
each of the Radiobuttons has to use a different value (we’ve used 0 and 1)

The communication through the switch object should work as follows:

selecting one of the Radiobuttons affects the switch object, which changes its
value to one of the possible values specified in the Radiobuttons’ constructor;
note: the mechanism works in the same way if there are more Radiobuttons in the group;
simultaneously, changing the switch object’s state affects the Radiobutton group.
As the switch is initially set to 1, we expect the second Radiobutton
(named Salad) to be selected when the application starts.

If you check/uncheck the Checkbutton, the Radiobutton group will follow the
change immediately and vice versa, while switching the active Radiobutton
inside the group will automatically check/uncheck the Checkbutton.
"""

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

radiobutton1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton2.pack()

window.mainloop()