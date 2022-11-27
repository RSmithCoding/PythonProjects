




from mimetypes import init
import os






class Main():


    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def clear():
        os.system('clear')    
        
    def main():
        Main.clear()                
        print("----------------------")
        print("1) Add a Customer")
        print("2) Print Details")
        print("q) Quit")
        print()
        choice = input("Please Select An Option: ")
        while choice != "q" or "1" or "2":
            if choice == "1":
                Main.add_customer()
            if choice == "2":
                Main.print_details()
            if choice == "q":
                quit()
            else:
                Main.main()            

    def add_customer():
        global name, number

        print("Customer Added")
        name = input("Name: ")
        number = input("Number: ")
        
        
        Main.main()

    def print_details():
        global name, number
        Main.clear()
        
        print(name)
        print(number)

        input("Press Any Key to Return to Main Menu...")


if __name__=='__main__':
    
    Main.main()
    pass