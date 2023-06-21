print("Welcome to the tip calculator.\n")
totalBill = input("What was the total bill?\n")
tip = input("What percentage would you like to tip? 10, 12 or 15?\n")
number_of_people = input("How many people to split the bill?\n")

billWithTip = (int(totalBill) + (int(totalBill)*((int(tip))/100)))

splitBill = "{:.2f}".format((billWithTip / int(number_of_people)))

print(f"Each person should pay ${splitBill}")
