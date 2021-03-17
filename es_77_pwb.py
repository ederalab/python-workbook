#multiplication table

print("     ", end="")
for n in range (1,10 +1):
    print("%5d" %n, end="")
print("\n")

for c in range (1,10 +1):
    print("%5d" %c, end="")
    for r in range (1, 10 +1):
        m = c*r
        if r % 10 == 0:
            print("%5d" %m , end="")
            print("\n")
        else:
            print("%5d" %m , end="")
print()
