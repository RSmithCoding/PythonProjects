import os
import collections
from fpdf import FPDF

sizes = []
takeSize = ""

def clear():
    os.system('clear')

clear()

print("Nosing Size Calculator - Press 'D' when done or 'R' to remove last item")
print()

while takeSize not in ("d","D"):
    takeSize = input("Please enter the Nosing Size then Enter (D when done) > ")
    if takeSize not in ("d","D","r","R"):
        sizes.append(takeSize)
        clear()
        print(*sizes)
        print("")
    if takeSize in ("R","r"):
        sizes.pop()
        clear()
        print(*sizes)
        print()
        continue    
    else:
        continue

clear()
print("Order Summery")    
print()
sizes.sort()

#print(*sizes)
#print()

total = sum(map(float, sizes))
quantity = collections.Counter(sizes)

print(f"Total Size... {total}")
print()
print("Size        Quantity")
print()
for key, value in quantity.items():
    print(f"{key}\t...\t{value}")


print()
choice = input("Would you like to print to PDF? Y/N > ")

    
dict = {"one":1,"two":2,"three":3}

list = [1,2,3,4,5]


if choice in ("y","Y"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Order Summery", ln=1, align="C")
    
    for i in list:
        pdf.write(5,str(i))
        pdf.ln()

    


    pdf.cell(200, 30, txt=str(total), ln=1, align="R")

    pdf.output("test.pdf")

    quit()
elif choice in ("N","n"):
    quit()
else:
    choice = input("Please enter Y/N... >")


