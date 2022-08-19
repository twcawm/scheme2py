from tkinter import *
from tkinter import ttk

root = Tk()
root.title("scheme2py")

L1 = Label(root,text="scheme string")
L1.pack(side=LEFT)

b = Button(root,text="eval")
b.pack(side=RIGHT)

E1=Entry(root,bd=5)
E1.pack(side=RIGHT)

root.mainloop()
