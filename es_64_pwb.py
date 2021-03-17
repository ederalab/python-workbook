#discount table
discount = 60
price = 4.95
while price <= 24.95:
    discount_amount = price * discount / 100
    discounted_price = price - discount_amount
    print("The original price is %.2f" %price)
    print("The discount amount is %.2f" %discount_amount)
    print("The discounted price is %.2f" %discounted_price,"\n")
    price = price + 5.00
