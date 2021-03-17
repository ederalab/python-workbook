#volume of cylinder
#area of circular base * height - round to one decimal

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = 2 * math.pi * radius * height

print ("The volume of the cylinder is %.1f" % volume)
