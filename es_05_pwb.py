#Bottle Deposit
less_than_1_liter = int(input("Number of bottles containing less than 1 liter: "))
more_than_1_liter = int(input("Number of bottles containing more than 1 liter: "))
deposit_less = 0.10
deposit_more = 0.25
total = less_than_1_liter * deposit_less + more_than_1_liter * deposit_more
total = "%.2f" % total
print(total)
