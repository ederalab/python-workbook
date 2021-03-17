#ideal gas law
"""
PV = nRT
P = pressure (Pascal) == 20000000
V = volume (liters) == 12
n = quantity of substance (moles)
R = ideal gas constant
T = temperature in °K == 20 + 273.15  °C > °K == (68 - 32) * 5/8) + 273.15 °F > °K
"""
R = 8.314 #J/mol K
K = 273.15

P = float(input("Enter the Pressure in Pascal: "))
V = float(input("Enter the Volume in liters: "))

TC = float(input("Enter the Temperature in Celsius degrees: "))
T = TC + K
n = P * V / R * T

#TF = float(input("Enter the Temperature in Farenheit degrees: "))
#T = (TF - 32) * 5/8 + K    
#n = P * V / R * T

print ("The amount of gas in moles is %.3f" % n)
