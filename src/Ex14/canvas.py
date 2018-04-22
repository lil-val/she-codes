from tkinter import *
"""Canvas is a way of creating a frame for drawing"""

root = Tk()

root.geometry('450x600+300+100')
root.title("My Canvas")

# the default color of the canvas is grey, as same that the window, the color should be changed in order to observed it
canvas1 = Canvas(root, height=300, width=300, bg="white")
canvas1.create_line(0, 0, 300, 300)  # defining start coordinate (0, 0 left top corner) and end coordinate (300, 300)
canvas1.create_oval(50, 150, 200, 250)  # required x1, y1, x2, y2, affect the width
canvas1.create_rectangle(50, 100, 150, 200)  # required x1, y1, x2, y2
coord = 10, 50, 240, 210  # we can mention it instead of coord in line #15
arc = canvas1.create_arc(coord, start=0, extent=300, fill="red")  # extent is the degree anti clockwise

canvas1.pack()  # pack only after drawing everything required

root.mainloop()
