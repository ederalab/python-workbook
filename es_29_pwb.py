#wind chill
#t = air temperature °C
#v = wind speed in km/h
t = float(input("Enter the air temperature in °C: "))
v = float(input("Enter the wind speed in km/h: "))
wci = 13.12 + (0.6125 * t) - (11.37 * (v**0.16)) + (0.3965 * t * (v**0.16))
print ("The wind chill is %1d" % wci)
