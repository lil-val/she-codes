from tkinter import *
from tkinter import messagebox


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(0.3048 * value)
    except ValueError:
        messagebox.showerror(message="Can't calculate meters for " + feet.get())


root = Tk()
root.title('Feet to Meters')
feet = StringVar()
meters = StringVar()
feet_entry = Entry(root, textvariable=feet).grid(row=0, column=1)
feet_label = Label(root, text='feet').grid(row=0, column=2)
equivalent_label = Label(root, text='is equivalent to').grid(row=1, column=0)
meters_value = Label(root, textvariable=meters).grid(row=1, column=1)
meter_label = Label(root, text='meters').grid(row=1, column=2)
calculate_button = Button(root, text='Calculate', command=calculate).grid(row=2, column=2)
root.mainloop()
