from io import TextIOBase
from tkinter import *


def getcount(count): 
    count = sec_entry.get()
    if(count.isdigit()):
        count = int(count)
        cdown(count)
    else:
        time_box.delete(0, 100)
        time_box.insert(0, "Incorrect time data")

def cdown(count):   
    if(count > 0):        
        time_box.delete(0, 100)
        time_box.insert(0, count)
        tdes.after(1000, cdown, count-1)
    else:
        time_box.delete(0, 100)
        time_box.insert(0, "This Worked!")
    

tdes = Tk()
tdes.geometry("500x500")
tdes.resizable(False,False)
tdes.rowconfigure(0,weight=1)
tdes.rowconfigure(1,weight=1)
tdes.rowconfigure(2,weight=1)
tdes.columnconfigure(0, weight=2)
tdes.columnconfigure(1, weight=1)
tdes.columnconfigure(2, weight=1)
tdes.columnconfigure(3, weight=1)
tdes.columnconfigure(4, weight=2)


#Shows numbers for timer
time_box = Entry(tdes, background="lightblue", font= ("aerial", 30))
time_box.grid(row=0, column=2, rowspan = 1) 

#label for the count down
t_label_seconds = Label(tdes, text = "Sec")
t_label_minutes = Label(tdes, text = "Min")
t_label_hours = Label(tdes, text = "hrs", font =("Helvetica", 16))

#label placement
t_label_seconds.grid(row=0, column = 3)

# entry of seconds 
sec_entry = Entry(tdes, background = "green", font= ("aerial", 30 ))
sec_entry.grid(row=1, column=3)

#entry of minutes 
min_entry = Entry(tdes, background="green", font= ("aerial", 30 )) 
min_entry.grid(row=1, column=2)

#entry of hours
hrs_entry = Entry(tdes, background="green", font= ("aerial", 30 )) 
hrs_entry.grid(row=1, column=1)

# Button to start timer
count = 10 #default of 10 sec set for count to initialise
start_button = Button(tdes, text = "Start Timer", command=lambda: getcount(count))
start_button.grid(row=2, column=1) 
tdes.mainloop()


