from tkinter import *
root = Tk()
sw = root.winfo_screenwidth()  # Return the number of pixels of the width of the screen of this widget in pixel
sh = root.winfo_screenheight()  # Return the number of pixels of the height of the screen of this widget in pixel
w = 300  # app width
h = 150  # app height
x = (sw - w) / 2
y = (sh - h) / 2
# root.geometry('width x height + offset from left + offset from top')
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.mainloop()

print(sw)
print(sh)
