
from tkinter import *
from tkinter import Tk

root = Tk()

root.title("Nosing Calculator")
root.resizable(FALSE,FALSE)
root.geometry("850x780")

#root.grid_rowconfigure(1, weight=1)
#root.grid_rowconfigure(2, weight=7)
#root.grid_rowconfigure(3, weight=1)
#root.grid_rowconfigure(4, weight=1)

"""HEADINGS"""
heading_frame = Frame(root, bg="blue")
heading_frame.grid(row=1, column=1, columnspan=5)

#heading_label = Label(heading_frame,text="Order Summary")
#heading_label.grid(row=1,column=0,columnspan=3)
#heading_label.config(font=("Arial",24))

#sub_heading_label = Label(heading_frame, text="Sizes Entered...")
#sub_heading_label.grid(row=0,column=3,columnspan=2)
#sub_heading_label.config(font=("Arial",24))

"""ORDER SUMMARY AREA"""
order_summary_frame = Frame(root, bg='green')
order_summary_frame.grid(row=2, column=1, columnspan=3)

#summary_label = Label(order_summary_frame,text="0.234   ...    x2")
#summary_label.grid(row=1,column=1)
#summary_label.config(font=("Arial",24))

"""SIZE LOG AREA"""
size_log_frame = Frame(root, bg='red')  
size_log_frame.grid(row=1, column=4, columnspan=2)

#size_log_label = Label(size_log_frame,text="0.242")
#size_log_label.grid(row=1,column=1)
#size_log_label.config(font=("Arial",24))

"""INPUT AREA"""
input_frame = Frame(root, bg='yellow')  
input_frame.grid(row=3, column=1, columnspan=5)

#size_entry = Entry(input_frame,width=20)
#size_entry.grid(row=2,column=0)
#size_entry.config(font=("Arial",24),justify="right")

#running_total = Label(input_frame, text="0",padx=100)
#running_total.grid(row=2,column=1)
#running_total.config(font=("Arial",24),justify="right")

# BUTTONS
buttons_frame = Frame(root, bg='orange')  
buttons_frame.grid(row=4, column=1, columnspan=5)

#pdf_button = Button(buttons_frame,text="Create PDF",padx=10,pady=10)
#pdf_button.grid(row=3, column=0)

#summary_button = Button(buttons_frame,text="Create Summary",padx=10,pady=10)
#summary_button.grid(row=3,column=1)

#remove_button = Button(buttons_frame,text="Remove Last Size",padx=10,pady=10)
#remove_button.grid(row=3,column=2)

#close_button = Button(buttons_frame,text="Close",padx=25,pady=10)
#close_button.grid(row=3,column=3)



root.mainloop()