import tkinter

root = tkinter.Tk()


def print_hi():
    print("hi")


button1 = tkinter.Button(root)
button1.config(text="morning tea soon",
               bg="green",
               fg="hotpink",
               font=("Papyrus", "50"),
               command=print_hi)
button1.grid()

root.mainloop()
