from tkinter import *
from tkinter import ttk

import schtoken
import schparser
import scheval

# initialize tokenizer and parser
tokenizer = schtoken.Tokenizer()
parser = schparser.Parser()


def evalCallback():
    str_in = userInput.get()
    tokenizer.set_input(str_in)
    parser.set_input(tokenizer.l_tokens)
    abstract_syntax_tree = parser.get_syntax_tree()
    str_out = scheval.evals(abstract_syntax_tree)
    print(str_out)


root = Tk()
root.title("scheme2py")

L1 = Label(root, text="scheme string")
L1.pack(side=LEFT)

b = Button(root, text="eval", command=evalCallback)
b.pack(side=RIGHT)

userInput = StringVar(root)
E1 = Entry(root, bd=5, textvariable=userInput)
E1.pack(side=RIGHT)

root.mainloop()
