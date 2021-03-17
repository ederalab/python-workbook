#distance units
# 1 foot = 12 inches
# 1 foot = 0.33 yards
# 1 foot = 0.000189394 miles
feet = float(input("Insert the distance in feet: "))
inches = feet * 12
yards = feet * 0.33
miles = feet * 0.000189394

print("The distance of ", feet, "feet equals: \n %.2f inches \n %.2f yards \n %.2f miles" % (inches, yards, miles))
