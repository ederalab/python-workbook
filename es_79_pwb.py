#greatest common divisor
m = int(input("Insert the first positive integer: "))
n = int(input("Insert the second positive integer: "))
d = min(n,m)

while (m % d != 0) or (n % d != 0):
    d = d-1

print("The greatest common divisor of",n,"and",m,"is",d)