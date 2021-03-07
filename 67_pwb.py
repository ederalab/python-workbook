#compute the perimeter of a polygon
from math import sqrt
"""
read x e y
untile empty x 
every time compute the distance from the first point
d = V (x2 - x1)**2 + (y2 - y1)**2
"""
x1 = input("Enter the first x coordinate: ")
y1 = input("Enter the first y coordinate: ")

x1 = float(x1)
y1 = float(y1)

xp = float(x1)
yp = float(y1)

p = 0 #perimeter

xi = input("Enter the next x coordinate (blank to quit): ")

while xi != "":
    y = input("Enter the next y coordinate: ")
    x = float(xi)
    y = float(y)
    d = sqrt( ((xp - x)**2) + ((yp - y)**2) ) #distance from previous point
    print("The distance from this point to the previous point is: ", d)
    p = p + d
    xp = float(x)
    yp = float(y)
    xi = input("Enter the next x coordinate (blank to quit): ")

d = sqrt( ((x1 - x)**2) + ((y1 - y)**2) ) #distance from first point
p = p + d
print("The perimeter of the polygon is: ", p)