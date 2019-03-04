from tkinter import *

root = Tk()
root.title("Lydia's Note Taker")
root.option_add("*font", "Consolas 20")
root.geometry("400x800")


def open_new_note():
    print("Open new note window")
    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.grid()

    title_label = Label(new_note_window,text="Title:")
    title_label.grid()

    title_entry = Entry(new_note_window)
    title_entry.grid()

    note_label = Label(new_note_window,text="Note text:")
    note_label.grid()

    note_entry = Entry(new_note_window)
    note_entry.grid()


def open_list(list_name):
    print("Open a list")


lbl_title = Label(root, text="Notes")
lbl_title.config(font=("Calibri", "30"), width=20)
lbl_title.grid(row=0, sticky=N + E + S + W)

btn_newnote = Button(root, text="+ New note", command=lambda: open_new_note())
btn_newnote.config()
btn_newnote.grid(row=1, sticky=W)

btn_shopping = Button(root, text="Shopping", command=lambda: open_list("Shopping"))
btn_shopping.config()
btn_shopping.grid(row=2, sticky=E + W)

btn_todo = Button(root, text="To do", command=lambda: open_list("To do"))
btn_todo.config()
btn_todo.grid(row=3, sticky=E + W)

btn_homework = Button(root, text="Homework", command=lambda: open_list("Homework"))
btn_homework.config()
btn_homework.grid(row=4, sticky=E + W)

root.mainloop()
