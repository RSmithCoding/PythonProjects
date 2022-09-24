# A small basic text based calculator

import math


#   Declare functions


def adding(num_1, num_2):
    add_answer = int(num_1) + int(num_2)
    return add_answer


def subtracting(num_1, num_2):
    sub_answer = int(num_1) - int(num_2)
    return sub_answer


def dividing(num_1, num_2):
    div_answer = int(num_1) / int(num_2)
    return div_answer


def multiplying(num_1, num_2):
    mul_answer = int(num_1) * int(num_2)
    return mul_answer


#   Display a welcome screen
print("*" * 50)
print("*" * 50)
print("**                                              **")
print("**                  Calculator                  **")
print("**                                              **")
print("*" * 50)
print("*" * 50)
print()
print()

#   Display menu

print("Please select from the following:")
print()
print("[1]  Addition")
print()
print("[2]  Subtracton")
print()
print("[3]  Division")
print()
print("[4]  Multiplication")
print()
choice = input("> ")

#   check input from menu

while choice != 1 or 2 or 3 or 4:
    if choice == "1":
        number_1 = input("Please enter your first number: ")
        number_2 = input("Please enter your second number: ")
        add_answer = adding(number_1, number_2)
        print(f"Your answers added together are: {add_answer}")
        break
    if choice == "2":
        number_1 = input("Please enter your first number: ")
        number_2 = input("Please enter your second number: ")
        sub_answer = subtracting(number_1, number_2)
        print(f"Your answers subtracted are: {sub_answer}")
        break
    if choice == "3":
        number_1 = input("Please enter your first number: ")
        number_2 = input("Please enter your second number: ")
        div_answer = dividing(number_1, number_2)
        print(f"Your answers divided are: {div_answer}")
        break
    if choice == "4":
        number_1 = input("Please enter your first number: ")
        number_2 = input("Please enter your second number: ")
        mul_answer = multiplying(number_1, number_2)
        print(f"Your answers multiplied are : {mul_answer}")
        break
    else:
        print("Please select another option")
        choice = input("> ")

print()
print("Good Bye")
