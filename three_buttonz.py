from tkinter import *

root = Tk()


def hello():
    labeltext.set("Hello!")


def banana():
    labeltext.set("Banana :/")


def clear():
    labeltext.set("")


labeltext = StringVar()
labeltext.set("")

button1 = Button(root)
button1.config(text="Say hello!", command=hello)
button1.grid()

button2 = Button(root)
button2.config(text="Say banana!", command=banana)
button2.grid()

button3 = Button(root)
button3.config(text="Clear text", command=clear)
button3.grid()

label1 = Label(root)
label1.config(textvariable=labeltext)
label1.grid()

root.mainloop()

