#fuel efficiency
#USA miles-per-gallon MPG
#Canada liters-per-hundred km L/100 km
#convert from MPG to L/100 km

mpg = float(input("Insert the fuel efficiency in MPG "))
lkm = 2.35215 
conversion = mpg / lkm

print ("%.2f" % conversion)
