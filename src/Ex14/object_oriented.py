from tkinter import *


class Window(Frame):  # Frame is class within tkinter

    def __init__(self, master=None):  # self is the object which referring to the class itself
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text="This is the first button")
        self.button1.grid()

        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text="This will show up text")

        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "This will also show text"


root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app = Window(root)

root.mainloop()
