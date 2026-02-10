from io import TextIOBase
from tkinter import *
import time

tdes = Tk()
tdes.geometry("500x500")
tdes.rowconfigure(0,weight=1)
tdes.rowconfigure(1,weight=1)
tdes.rowconfigure(2,weight=1)
tdes.columnconfigure(0, weight=1)
tdes.columnconfigure(1, weight=1)
tdes.columnconfigure(2, weight=1)
time_box = Text(tdes, background="lightblue")

#taking time values for eventual timer
old_time = time.time()
task_duration = 10
time.sleep(task_duration)
new_time = time.time()
elapse = new_time-old_time
print(f"time: {old_time:.2f}")
print(f"New time: {new_time:.2f} \nTime elapsed = {elapse:.2f}")
time_box.insert("1.0", f"seconds this epoch: {new_time}")
time_box.configure()
time_box.grid(row=1, column=1, rowspan=1, columnspan=1)
tdes.mainloop()
