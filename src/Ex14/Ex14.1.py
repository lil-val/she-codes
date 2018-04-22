import time
from datetime import datetime
from tkinter import *
import pytz


root = Tk()
root.title('Clock')
"""canvas = Canvas(root, width=400, height=200)
timetext = canvas.create_text(200, 100, text=time.asctime(), font=('Helvetica', 20))
canvas.pack()
while True:
    canvas.itemconfig(timetext, text=time.asctime())
    canvas.update()
"""

time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)


def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


tick()
root.mainloop()


current_time = datetime.now(pytz.timezone('Asia/Shanghai'))
print(datetime.now())
print(current_time.strftime('%H:%M:%S'))
print(datetime.now(pytz.timezone('Israel')))
print(datetime.now(pytz.timezone('US/Pacific')))
print(datetime.now(pytz.timezone('Europe/London')))
