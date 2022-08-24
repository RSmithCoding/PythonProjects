#   This is a small application which works out how many packs of laminate flooring you will need and cost
#   based on the price, area to be covered, and the coverage of the laminate bought.

import math

print("*" * 50)
print("*" * 50)
print("**                                              **")
print("**         Laminate Flooring Calculator         **")
print("**                                              **")
print("*" * 50)
print("*" * 50)
print()
print()

cost = input("How much does the laminate cost per m2? >")

print()
pack_size = input("What is the pack size of the laminate in m2? >")

print()
area = input("What is the area to be covered in m2? >")
print()
print()
print()


no_of_packs = float(area) / float(pack_size)

price = math.ceil(no_of_packs) * float(cost)


print(f"You will need {math.ceil(no_of_packs)} packs of laminate")
print()

print(f"The total cost of your laminate will be £{price:.2f}")
print()
print()
print()

