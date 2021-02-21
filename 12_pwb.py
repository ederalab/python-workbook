#distance between 2 points on earth
#get the latitude and longitude (t1,g1) - (t2,g2)
#display the distance between the points 

import math

lt1 = float(input("Enter latitude point A: "))
lg1 = float(input("Enter longitude point A: "))
lt2 = float(input("Enter latitude point B: "))
lg2 = float(input("Enter longitude point B: "))

t1 = math.radians(lt1)
g1 = math.radians(lg1)
t2 = math.radians(lt2)
g2 = math.radians(lg2)

distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("The distance between point A and point B is %.4f km following the surface of Earth" % distance)