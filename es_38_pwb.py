#name that shape
sides = int(input("Insert the number of sides: "))

if sides == 3:
    print("The shape is a triangle")
elif sides == 4:
    print("The shape is a square")
elif sides == 5:
    print("The shape is a pentagon")
elif sides == 6:
    print("The shape is a hexagon")
elif sides == 7:
    print("The shape is a heptagon")
elif sides == 8:
    print("The shape is a octagon")
elif sides == 9:
    sides("The shape is a ennagon")
elif sides == 10:
    sides("The shape is a decagon")
elif sides > 0 and sides < 3:
    print("This isn't a shape, ")
    if sides == 2:
        print("this is a line!")
    else:
        print("this is a point!")
elif sides <= 0:
    print("Please insert a correct positive number, greater than 3")
else:
    print("The shape is a polygon with", sides, "sides")
