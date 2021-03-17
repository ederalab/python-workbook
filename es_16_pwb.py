#area and volume
#read radius, compute and display the area of circle and the volume of a sphere
#area = p*r2 volume = 4/3 pi r3

import math
r = float(input("Insert radius: "))
area = math.pi * r**2
volume = 4/3 * math.pi * r**3

print("With a radius of ", r, "the area of the circle is %.3f" % area, "and the volume is %.3f" % volume)
