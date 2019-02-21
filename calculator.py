from tkinter import *

root = Tk()
root.title("Mr Harford's Calculator")
root.option_add("*font", "Cambria 20")


def add_to_input_text(next_value):
    current_text = input_text.get()
    input_text.set(current_text + next_value)


def calculate_answer():
    ans = eval(input_text.get())
    answer_value.set(ans)


def clear():
    input_text.set("")
    answer_value.set("")


input_text = StringVar()
input_text.set("")

answer_value = StringVar()
answer_value.set("")

button1 = Button(root, text="7", width=3, command=lambda: add_to_input_text("7")).grid(row=0, column=0, sticky=N+E+S+W)
button1 = Button(root, text="8", width=3, command=lambda: add_to_input_text("8")).grid(row=0, column=1, sticky=N+E+S+W)
button1 = Button(root, text="9", width=3, command=lambda: add_to_input_text("9")).grid(row=0, column=2, sticky=N+E+S+W)
button1 = Button(root, text="4", width=3, command=lambda: add_to_input_text("4")).grid(row=1, column=0, sticky=N+E+S+W)
button1 = Button(root, text="5", command=lambda: add_to_input_text("5")).grid(row=1, column=1, sticky=N+E+S+W)
button1 = Button(root, text="6", command=lambda: add_to_input_text("6")).grid(row=1, column=2, sticky=N+E+S+W)
button1 = Button(root, text="1", width=3, command=lambda: add_to_input_text("1")).grid(row=2, column=0, sticky=N+E+S+W)
button1 = Button(root, text="2", command=lambda: add_to_input_text("2")).grid(row=2, column=1, sticky=N+E+S+W)
button1 = Button(root, text="3", command=lambda: add_to_input_text("3")).grid(row=2, column=2, sticky=N+E+S+W)
button1 = Button(root, text="0", command=lambda: add_to_input_text("0")).grid(row=3, column=0, sticky=N+E+S+W)

button1 = Button(root, text="+", width=3, command=lambda: add_to_input_text("+")).grid(row=0, column=3, sticky=N+E+S+W)
button1 = Button(root, text="-", command=lambda: add_to_input_text("-")).grid(row=1, column=3, sticky=N+E+S+W)
button1 = Button(root, text="*", command=lambda: add_to_input_text("*")).grid(row=2, column=3, sticky=N+E+S+W)
button1 = Button(root, text="/", command=lambda: add_to_input_text("/")).grid(row=3, column=3, sticky=N+E+S+W)

button1 = Button(root, text="=", command=lambda: calculate_answer()).grid(row=3, column=1, columnspan=2, sticky=N+E+S+W)

input_area = Label(root, textvariable=input_text, bg="hotpink", fg="white").grid(row=4, column=0, columnspan=4, sticky=N+E+S+W)
answer_area = Label(root, textvariable=answer_value, bg="dodgerblue", fg="white").grid(row=5, column=0, columnspan=4, sticky=N+E+S+W)

clear_button = Button(root, text="Clear", command=lambda: clear()).grid(row=6, column=0, columnspan=4, sticky=N+E+S+W)

root.mainloop()
