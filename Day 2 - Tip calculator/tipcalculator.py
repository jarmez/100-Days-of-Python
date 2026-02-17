#!/bin/python
# Solution shows two ways of diong this, final statement calculating bill in one statement
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# tip_as_percentage = tip /100
# tip_total = bill * tip_as_percentage
# bill_total = bill + tip_total
# bill_per_person = bill_total / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")
print("Each person should pay: $" + str(round((bill * (1 + (tip / 100)) / people), 2)))
