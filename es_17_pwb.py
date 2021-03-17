#heat capacity
""" 
q = energy - C = heat capacity - m = mass grams q = m C deltaT
read the mass and the temperature change
display the amount of energy that must be added or remove to achieve desired temperature change
capacity of water = 4.186 * J/g°C (water have grams == milliliters)
"""
m = float(input("Enter the mass of water: "))
t = float(input("Enter the temperature change: "))
C = 4.186
q = m * C * t
print("The energy you need to achieve the temperature is %.2f" % q, " J")

"""
extend the program adding the cost of heating the water
electricity = 8.9 cents per kilowatt hour 
1 Joule = 2,77778e-7 KWh
"""
kwh =  q * 2.77778*10**-7 
cost = 8.9 * kwh

print("\n The cost is %.2f" % cost, " $ per KWh")
