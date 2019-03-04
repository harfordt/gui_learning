from tkinter import *

root = Tk()

red = Label(root, text="Red", fg="white", bg="red").grid(row=0, column=0, rowspan=2, sticky=N + S)
blue = Label(root, text="Blue", fg="white", bg="blue", height=20, width=100).grid(row=0, column=1, padx=50, pady=50)
green = Label(root, text="Green", fg="white", bg="green").grid(row=1, column=1, sticky=E + W)

root.mainloop()