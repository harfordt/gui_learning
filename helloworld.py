import tkinter	     # imports the tkinter library
root = tkinter.Tk() # creates a Tk object (a 'window')

root.title("Hello World!!!")	# sets the title of the window
root.geometry("600x200")    	# sets the window's width and height


#create a label
my_label = tkinter.Label(root)   #creates a label and attaches it to the window
my_label.config(text="Hello!", fg="green")  # options to configure the label
my_label.grid()        # a special method for placing the widget on the window

root.mainloop()

