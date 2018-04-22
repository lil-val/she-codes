from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Bla Bla Bla")   # contain an ok button

answer = tkinter.messagebox.askquestion("Question 1", "Do you like chocolate?")

if answer == 'yes':
    print('Chocolate!!!')

root.mainloop()
