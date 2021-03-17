#tax and tip
#reading the cost of a meal with tax (local) and tip (18% of the meal without tax)
#output tax amount, tip amount, grand total with 2 decimal

meal_cost = float(input("The cost of the meal is:"))
tax = meal_cost * 22 / 100
tip = meal_cost * 18 / 100
grand_total = meal_cost + tax + tip

print("The tax amount is %.2f, the tip amount is %.2f and the total amount is %.2f" % (tax, tip, grand_total))
