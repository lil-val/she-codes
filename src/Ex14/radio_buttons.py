from tkinter import *


class Application(Frame):

    def __init__(self, master):
        """initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """create widgets for movie type choices"""
        Label(self, text="Choose your favorite type of movie"
              ).grid(row=0, column=0, sticky=W)
        Label(self, text="Selecting one:"
              ).grid(row=1, column=0, sticky=W)
        #  variable for single, favorite type of movie
        self.favorite = StringVar()
        Radiobutton(self, text="Comedy", variable=self.favorite, value="comedy.", command=self.update_text
                    ).grid(row=2, column=0, sticky=W)
        Radiobutton(self, text="Drama", variable=self.favorite, value="drama.", command=self.update_text
                    ).grid(row=3, column=0, sticky=W)
        Radiobutton(self, text="Romance", variable=self.favorite, value="romance.", command=self.update_text
                    ).grid(row=4, column=0, sticky=W)
        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """update the text area"""
        message = "Your favorite type of movie is "
        message += self.favorite.get()
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)


root = Tk()
root.title("Movie chooser 2")
app = Application(root)
root.mainloop()
