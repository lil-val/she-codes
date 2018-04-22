from tkinter import *


class Application(Frame):

    def __init__(self, master):
        """initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """create widgets for movie type choice"""
        Label(self, text="Choose your favorite movie type").grid(row=0, column=0, sticky=W)

        # instructions
        Label(self, text="Select all that apply:").grid(row=1, column=0, sticky=W)

        # comedy check button
        self.comedy = BooleanVar()
        Checkbutton(self, text="Comedy", variable=self.comedy, command=self.update_text).grid(row=2, column=0, sticky=W)

        # drama check button
        self.drama = BooleanVar()
        Checkbutton(self, text="Drama", variable=self.drama, command=self.update_text).grid(row=3, column=0, sticky=W)

        # romance check button
        self.romance = BooleanVar()
        Checkbutton(self, text="Romance", variable=self.romance, command=self.update_text).grid(row=4, column=0, sticky=W)

        self.result = Text(self, width=40, height=5, wrap=WORD)  # wrap=WORD when dropping 1 line down the words will not cut in the middle, drop line prior or after word end
        self.result.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """update text widget and display favorite movie types"""
        likes = ""
        if self.comedy.get():
            likes += "You like comedy."
        if self.drama.get():
            likes += "You like drama."
        if self.romance.get():
            likes += "You like romantic."
        self.result.delete(0.0, END)  # delete from position 0 until the end
        self.result.insert(0.0, likes)  # insert to textbox the text in likes in position 0


root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()
