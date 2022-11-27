
from tkinter import *
from tkinter import Tk

root = Tk()

root.title("Nosing Calculator")
root.resizable(FALSE,FALSE)
root.geometry("850x780")

heading_frame = Frame(root, height=20, width=850, padx=0, pady=0)
heading_frame.grid(row=0, columnspan=5)

heading_label = Label(heading_frame,text="Nosing Calculator")
heading_label.grid(row=0, column=0)
heading_label.config(font=("Arial",24))

sub_heading_label = Label(heading_frame, text="Sizes Entered...")
sub_heading_label.grid(row=0, column=1)
sub_heading_label.config(font=("Arial",24))

order_summery_frame = Frame(root, height=500, width=700,bg='#93c47d')   #green
order_summery_frame.grid(row=1, rowspan=3, column=0, columnspan=3)

input_frame = Frame(root, height=40, width=700,bg='#E6337A')    #pink
input_frame.grid(row=4, column=0, rowspan=1, columnspan=3)

buttons_from = Frame(root, height=40, width=700,bg='#2986cc')   #blue
buttons_from.grid(row=5, column=0, rowspan=1, columnspan=3)

size_log_frame = Frame(root, height=760, width=150,bg='#cc0000')    #red
size_log_frame.grid(row=1, column=4 ,rowspan=3, columnspan=2)

root.mainloop()