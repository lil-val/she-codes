from tkinter import *
"""only 1 radio button is enabled at a time"""

root = Tk()
"""the values are used as indexes, individual button that only 1 will be selected at a given time
if 2 buttons have the same value while choosing 1 of them the second will be selected also """
radio_1 = Radiobutton(root, text="option 1", value=1, variable=1).pack()
radio_2 = Radiobutton(root, text="option 2", value=2, variable=1).pack()
radio_3 = Radiobutton(root, text="option 3", value=3, variable=1).pack()
"""if we would like to split the buttons into 2 separate groups in order to select 1 from each group,
',variable=1' group the buttons together (instead of =1 we can use any number or string)"""
radio_4 = Radiobutton(root, text="option 4", value=4, variable=2).pack()
radio_5 = Radiobutton(root, text="option 5", value=5, variable=2).pack()
radio_6 = Radiobutton(root, text="option 6", value=6, variable=2).pack()

root.mainloop()
