from tkinter import *
import tkinter.messagebox


def m_quit():
    m_exit = tkinter.messagebox.askyesno(title="Quit", message="Are you sure?")
    if m_exit > 0:  # True
        root.destroy()
        return


root = Tk()

tkinter.messagebox.showinfo(title="About", message="This is my About Box")  # info icon
tkinter.messagebox.showwarning(title="About", message="This is my About Box")  # warning icon
tkinter.messagebox.showerror(title="About", message="This is my About Box")  # error icon
tkinter.messagebox.askquestion()
tkinter.messagebox.askokcancel()
tkinter.messagebox.askyesno()
tkinter.messagebox.askretrycancel()
