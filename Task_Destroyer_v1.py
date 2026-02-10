from io import TextIOBase
from tkinter import *
import datetime
import time


def Sandout(count):
    if(count > 0):        
        time_box.delete("1.0", END)
        time_box.insert("1.0", count)
        tdes.after(1000, Sandout, count-1)
    else:
        time_box.delete("1.0, END")
        time_box.insert("1.0", "This Worked!")

tdes = Tk()
tdes.geometry("500x500")
tdes.rowconfigure(0,weight=1)
tdes.rowconfigure(1,weight=1)
tdes.rowconfigure(2,weight=1)
tdes.columnconfigure(0, weight=1)
tdes.columnconfigure(1, weight=1)
tdes.columnconfigure(2, weight=1)
time_box = Text(tdes, background="lightblue", font=("Aerial", 50 ), fg = "green")
time_box.grid(row=1, column=1, rowspan=1, columnspan=1)
sec_entry = Entry(tdes)
sec_entry.grid(row=2, column=1, rowspan=1, columnspan=1)
count = 10

Sandout(count) 
tdes.mainloop()





"""taking time values for eventual real timer??

display_time = old_time.strftime("%X")
print(f"current time: {display_time}")
time.sleep(10)
new_time = datetime.datetime.now()
display_time= new_time.strftime("%X")
print(f"current time: {display_time}")
time_box.insert("1.0", f"Current Time: {display_time}") """


