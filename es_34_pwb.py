#day old bread
bread = 3.49
day_old_discount = 60
loaves = int(input("Insert how many loaves have been purchased: "))
regular_price = bread * loaves
discounted_price = bread * (day_old_discount / 100) * loaves
total_price = regular_price - discounted_price
print("If you buy",loaves,"loaves")
print("The regular price is    %5.2f$" % regular_price)
print("The discounted price is %5.2f$" % discounted_price)
print("The total price is      %5.2f$" % total_price)
