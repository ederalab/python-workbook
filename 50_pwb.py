#richter scale

magnitude = float(input("Insert the magnitude: "))

if magnitude < 2.0:
    descriptor = "micro"
elif magnitude >= 2.0 and magnitude < 3.0:
    descriptor = "very minor"
elif magnitude >= 3.0 and magnitude < 4.0:
    descriptor = "minor"
elif magnitude >= 4.0 and magnitude < 5.0:
    descriptor = "light"
elif magnitude >= 5.0 and magnitude < 6.0:
    descriptor = "moderate"
elif magnitude >= 6.0 and magnitude < 7.0:
    descriptor = "strong"
elif magnitude >= 7.0 and magnitude < 8.0:
    descriptor = "major"
elif magnitude >= 8.0 and magnitude < 10.0:
    descriptor = "great"
else:
    descriptor = "meteoric"

print("A magnitude of",magnitude,"is considered to be a",descriptor,"earthquake")