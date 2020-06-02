#example using pack geometry manager

from tkinter import *
root = Tk()

parent = Frame(root)
#placing widget top-down
Button(parent,text="All is Well").pack(fill=X)
Button(parent,text="Back to Basics").pack(fill=X)
Button(parent,text="Catch me if you can").pack(fill=X)
#placing widgets side by side
Button(parent,text="LEFT").pack(side=LEFT)
Button(parent,text="CENTER").pack(side=LEFT)
Button(parent,text="RIGHT").pack(side=LEFT)

parent.pack()
root.mainloop()