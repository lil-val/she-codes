from tkinter import *

root = Tk()  # creating an application (window)

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

bottom1 = Button(top_frame, text='Bottom 1', fg='red')
bottom2 = Button(top_frame, text='Bottom 2', fg='blue')
bottom3 = Button(top_frame, text='Bottom 3', fg='green')
bottom4 = Button(bottom_frame, text='Bottom 4', fg='purple')

bottom1.pack(side=LEFT)
bottom2.pack(side=LEFT)
bottom3.pack(side=LEFT)
bottom4.pack()  # since there is only one bottom the positioning is not required

root.mainloop()  # the app run in loop, waiting for events
