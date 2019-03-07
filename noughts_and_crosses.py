from tkinter import *

root = Tk()

root.title("Noughts and Crosses")
root.option_add("*font", "Consolas 30")

next = "X"


def turn(button):
    global next
    print("A player has taken a turn")
    if button.get() in ["X", "O"]:
        return
    button.set(next)
    if next == "X":
        next = "O"
    else:
        next = "X"


b1_text = StringVar()
b2_text = StringVar()
b3_text = StringVar()
b4_text = StringVar()
b5_text = StringVar()
b6_text = StringVar()
b7_text = StringVar()
b8_text = StringVar()
b9_text = StringVar()

b1 = Button(root, textvariable=b1_text, width=6, height=3, command=lambda: turn(b1_text)).grid(row=0, column=0)
b2 = Button(root, textvariable=b2_text, width=6, height=3, command=lambda: turn(b2_text)).grid(row=0, column=1)
b3 = Button(root, textvariable=b3_text, width=6, height=3, command=lambda: turn(b3_text)).grid(row=0, column=2)
b4 = Button(root, textvariable=b4_text, width=6, height=3, command=lambda: turn(b4_text)).grid(row=1, column=0)
b5 = Button(root, textvariable=b5_text, width=6, height=3, command=lambda: turn(b5_text)).grid(row=1, column=1)
b6 = Button(root, textvariable=b6_text, width=6, height=3, command=lambda: turn(b6_text)).grid(row=1, column=2)
b7 = Button(root, textvariable=b7_text, width=6, height=3, command=lambda: turn(b7_text)).grid(row=2, column=0)
b8 = Button(root, textvariable=b8_text, width=6, height=3, command=lambda: turn(b8_text)).grid(row=2, column=1)
b9 = Button(root, textvariable=b9_text, width=6, height=3, command=lambda: turn(b9_text)).grid(row=2, column=2)

reset_button = Button(root, text="Reset", width=6, height=3).grid(row=3, column=0, columnspan=3, sticky=E + W)

root.mainloop()
