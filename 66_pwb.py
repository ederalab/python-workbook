#no more pennies
price = input("Insert the price: ")

pennies = 5
nickels = 0.05

total = 0.0
while price != "":
    total = total + float(price)
    price = input("Insert the price: ")

print ( "The total price is: %.02f" % total) 

remainder = total * 100 % pennies
if remainder < 2.5:
    cash = total - remainder / 100
else:
    cash = total + nickels - remainder / 100

print ( "The price if you pay cash is : %.02f" % cash) 
