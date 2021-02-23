#free fall

import math

d = float(input("Enter the height from which the object is dropped: "))
vi = 0
a = 9.8

vf = math.sqrt(vi**2 + (2 * a* d))
print ("The final speed is %.2f m/s" % vf)