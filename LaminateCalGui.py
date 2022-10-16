# This is a gui version of the console application i created to price up laminate flooring

import math
from tkinter import *
from tkinter import Tk
from tkinter import messagebox


root = Tk()

root.title("Laminate Price Calculator")
root.resizable(FALSE,FALSE)
appwidth = 300
appheight = 400
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x = (screenwidth / 2) - (appwidth / 2)
y = (screenheight / 2) - (appheight / 2)

root.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")

def calculate():

    try:
        float(entry1.get()) or int(entry1.get())
    except ValueError:
        messagebox.showinfo(message="Please enter the cost per M2")
    
    try:
        float(entry2.get()) or int(entry2.get())
    except ValueError:
        messagebox.showinfo(message="Please enter the correct pack size")    
    
    try:
        float(entry3.get()) or int(entry3.get())
    except ValueError:
        messagebox.showinfo(message="Please enter the correct area in M2")    
    
    cost = entry1.get()
    area = entry3.get()
    pack_size = entry2.get()
        
    no_of_packs = float(area) / float(pack_size)

    price = math.ceil(no_of_packs) * float(cost)

    label4 = Label(frame1,text=f"You will need {math.ceil(no_of_packs)} Packs")
    label4.grid(column=0,row=8,sticky='w',pady=2, padx=30)
    label5 = Label(frame1,text=f"The Total Cost is £{price:.2f}")
    label5.grid(column=0,row=9,sticky='w',pady=2, padx=30)
  
    



frame1 = Frame(root)
frame1.grid(column=0,row=0, sticky='n,s,e,w',padx=15,pady=15)

label1 = Label(frame1,text="Cost of Laminate per M2...")
label1.grid(column=0, row=1,sticky='w',pady=2, padx=30)

entry1 = Entry(frame1)
entry1.grid(column=0, row=2,sticky='w,e',pady=2, padx=30)

label2 = Label(frame1,text="Pack size per M2...")
label2.grid(column=0, row=3,sticky='w',pady=2, padx=30)

entry2 = Entry(frame1)
entry2.grid(column=0, row=4,sticky='w,e',pady=2, padx=30)

label3 = Label(frame1,text="Area to be covered in M2...")
label3.grid(column=0, row=5,sticky='w',pady=2, padx=30)

entry3 = Entry(frame1)
entry3.grid(column=0, row=6,sticky='w,e',pady=2, padx=30)

buttonCalculate = Button(frame1,text="Calculate...",command=calculate).grid(column=0,row=7,sticky='e,w',pady='20',padx='30')

entry1.focus()

root.mainloop()