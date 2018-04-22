from tkinter import *


def do_nothing():
    print("ok")


root = Tk()

# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)  # configuring a menu name "menu", it is located automatically

sub_menu = Menu(menu)  # submenue inside menu
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New Project", command=do_nothing)
sub_menu.add_command(label="New", command=do_nothing)
sub_menu.add_separator()  # adding line to separate groups of items in the menu
sub_menu.add_command(label="Exit", command=do_nothing)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=do_nothing)


# ***** Toolbar *****

toolbar = Frame(root, bg="blue")  # creating a frame in the main window with background
insert_button = Button(toolbar, text="Insert Image", command=do_nothing)
insert_button.pack(side=LEFT, padx=2, pady=2)  # locate the button. pad create extra space
print_button = Button(toolbar, text="Print", command=do_nothing)
print_button.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)  # display toolbar on the top, below the menu, make it as wider as the window


# ***** Status Bar *****
# status b ar is located at the bottom of the window, it is usually changed

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)  # bd = border around the label, sunk in the window, text on the left
status.pack(side=BOTTOM, fill=X)

root.mainloop()

