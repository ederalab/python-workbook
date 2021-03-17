#units of pressure
#1 kp = 0,145038 pounds per square inches
#1 kp = 7,50062 mm of mercury
#1 kp = 0,0098692382432766 atm

kilo_pascals = float(input("Enter pressure in kilo-pascal: "))
pounds_per_square_inches = kilo_pascals * 0.145038
millimeters_of_mercury = kilo_pascals * 7.50062
atmospheres = kilo_pascals * 0.0098692382432766

print ("The pressure of %.3f kilo-pascals is equal to \n%.3f pounds per inches\n%.3f millimeters of mercury\n%.3f atmosphere" % (kilo_pascals, pounds_per_square_inches, millimeters_of_mercury, atmospheres) )
