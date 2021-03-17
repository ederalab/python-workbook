#approximate pi greco
pi = 3
a = 2
b = 3
c = 4

for n in range(1,15):
    if n % 2 != 0:
        pi += 4/(a*b*c)
    else:
        pi -= 4/(a*b*c)
    a += 2
    b += 2
    c += 2

print(pi)

