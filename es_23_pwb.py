#area of regular polygon
import math
s = float(input("Insert the length a side: "))
n = float(input("Insert the number of sides: "))

area = n * s**2 / 4 * math.tan(math.pi / n)

print ("The matharea of this polygon is %.3f" % area)
