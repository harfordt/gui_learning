class Note:
    """

    """

    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        """Getter function: gets the note title

        Returns: the title of the note

        """
        return self.__title

    def get_text(self):
        """Getter function: gets the note body text

        Returns: the body text of the note

        """
        return self.__text

    def get_category(self):
        """Getter function: gets the note category

        Returns: the category of the note

        """
        return self.__category


from tkinter import *

# creates and sets up the window
root = Tk()
root.title("Lydia's Note Taker")
root.option_add("*font", "Consolas 20")
root.geometry("400x800")

# this list is where all note objects will be stored
notes = []


def save_note(window, title, body, category):
    """Saves a note to the note list then closes the parent window.

    Args:
        window: the window this function was called from
        title: the title of the note to be saved
        body: the body text of the note to be saved
        category: the category of the note to be saved
    """

    # creates the note object, after cleaning up the input values
    new_note = Note(title.capitalize().strip(),
                    body.capitalize().strip(),
                    category.capitalize().strip())

    # add the note to the note list
    notes.append(new_note)
    # print("Title: {}".format(new_note.get_title()))
    # print("Body: {}".format(new_note.get_text()))
    # print("Category: {}".format(new_note.get_category()))

    # close the window this function was called from
    window.destroy()


def open_new_note(category):
    """Creates a window for the user to enter their note in."""
    print("Open new note window")
    title_value = StringVar()

    # creates the window
    new_note_window = Toplevel(root)

    # creates and adds labels and text entry areas
    new_note_title = Label(new_note_window, text="New {} Note".format(category))
    new_note_title.grid()

    title_label = Label(new_note_window, text="Title:")
    title_label.grid(sticky=W)

    title_entry = Entry(new_note_window, textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note text:")
    note_label.grid(sticky=W)

    note_text = Text(new_note_window)
    note_text.config(height=10, width=20)
    note_text.grid()

    # a frame allows us to group GUI elements together
    # this one will hold the buttons
    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="Cancel", command=new_note_window.destroy)
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame,
                         text="Save",
                         command=lambda: save_note(new_note_window,
                                                   title_value.get(),
                                                   note_text.get(1.0, END),
                                                   category))

    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_category):
    """Opens a window with all of the notes of the given category.

    Args:
        list_category: the category this window should display
    """
    print("Open {}".format(list_category))

    # creates and formats the window
    list_window = Toplevel(root)
    list_window.title(list_category)
    list_window.geometry("600x400")

    # takes each note from the list, formats it and adds it to the window
    for note in notes:
        category = note.get_category()

        # only add notes with the relevant category
        if category == list_category:
            title = note.get_title()
            body = note.get_text()
            note_text = "***{}***\n{}\n".format(title, body)
            Label(list_window, text=note_text).grid(sticky=W)


"""
    The main (root) window is configured from here down.
    It is not in a function so all widgets etc are globally accessible.
"""
lbl_title = Label(root, text="Notes")
lbl_title.config(font=("Calibri", "30"), width=18)
lbl_title.grid(row=0, sticky=N + E + S + W)

btn_shopping = Button(root, text="Shopping", command=lambda: open_list("Shopping"))
btn_shopping.config()
btn_shopping.grid(column=0, row=1, sticky=E + W)

btn_shopping_new = Button(root, text="+", command=lambda: open_new_note("Shopping"))
btn_shopping_new.config()
btn_shopping_new.grid(column=1, row=1, sticky=E + W)

btn_todo = Button(root, text="To do", command=lambda: open_list("To do"))
btn_todo.config()
btn_todo.grid(column=0, row=2, sticky=E + W)

btn_todo_new = Button(root, text="+", command=lambda: open_new_note("To do"))
btn_todo_new.config()
btn_todo_new.grid(column=1, row=2, sticky=E + W)

btn_homework = Button(root, text="Homework", command=lambda: open_list("Homework"))
btn_homework.config()
btn_homework.grid(column=0, row=3, sticky=E + W)

btn_homework_new = Button(root, text="+", command=lambda: open_new_note("Homework"))
btn_homework_new.config()
btn_homework_new.grid(column=1, row=3, sticky=E + W)

# this needs to be the last line - anything after this won't be seen
root.mainloop()
