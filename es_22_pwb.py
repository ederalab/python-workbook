#area of triangle
import math
s1 = float(input("Insert the length of side 1: "))
s2 = float(input("Insert the length of side 2: "))
s3 = float(input("Insert the length of side 3: "))
s = (s1 + s2 + s3)/2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print ("The area of this triangle is %.3f" % area)
