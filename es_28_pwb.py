#body mass index
weight = float(input("Insert your weight in kg: "))
height = float(input("Insert your height in cm: "))
height = height / 100 #m
bmi = weight / (height * height)
print ("Your body mass index is %.2f" % bmi)
