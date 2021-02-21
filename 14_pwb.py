#height units
foot = 12 #inches
inch = 2.54 #cm

feet = int(input("Insert yout height - foot first: "))
inches = float(input("than inches: "))

conversion_inches = feet * foot
height = inches + conversion_inches

height_cm = height * inch

print("Your height is %0.2f" % height_cm, " cm")