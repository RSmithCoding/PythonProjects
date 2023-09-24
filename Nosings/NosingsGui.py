
from tkinter import *
from tkinter import Tk

root = Tk()

root.title("Nosing Calculator")
root.resizable(FALSE,FALSE)
root.geometry("550x780")

mainframe = Frame(root,height=780, width=550)
mainframe.grid(column=1,row=1)
mainframe.grid_rowconfigure(1,weight=1)
mainframe.grid_rowconfigure(2,weight=7)
mainframe.grid_rowconfigure(3,weight=1)
mainframe.grid_rowconfigure(4,weight=1)

"""HEADING LABELS"""
heading1 = Label(mainframe,font=("Arial",24),text="Nosing Order Summary")
heading1.grid(column=1, columnspan=2, row=1,)

heading2 = Label(mainframe,font=("Arial",24),text="Sizes Entered...")
heading2.grid(column=3, columnspan=2, row=1)

"""ORDER SUMMARY"""
order_summary = Label(mainframe, font=("Arial",18), text="""
0.234   ....    x1
0.544   ....    x1
0.534   ....    x3""")
order_summary.grid(column=1, columnspan=2,row=2,pady=(10,500))

"""SIZES ENTERED"""
sizes_entered = Label(mainframe, font=("Arial",18), text="""
0.543
0.345
0.355
0.355""")
sizes_entered.grid(column=3, columnspan=2, row=2,pady=(10,500))

"""ENTRY / TOTAL"""

entry = Entry(mainframe,width=20,font=("Arial",24),justify="right")
entry.grid(column=1,columnspan=2,row=3,pady=(0,20))

total = Label(mainframe, text="0.234",font=("Arial",24))
total.grid(column=3, columnspan=2,row=3,sticky="e",pady=(0,20))

"""BUTTONS"""

pdf_button = Button(mainframe, text="Create PDF", padx=5, pady=20)
pdf_button.grid(column=1,row=4,sticky="e,w,s")

create_summary_button = Button(mainframe, text="Create Order Summary",padx=5, pady=20)
create_summary_button.grid(column=2,row=4,sticky="e,w,s")

remove_last_button = Button(mainframe, text="Remove Last Size",padx=5,pady=20)
remove_last_button.grid(column=3,row=4,sticky="e,w,s")

close_button = Button(mainframe, text="Close",padx=5, pady=20)
close_button.grid(column=4,row=4,sticky="e,w,s")

root.mainloop()