#temperature conversion table 0 C = 32 F
print("  T°C  |  T°F")
t = 0
while t <= 100:
    tf = t + 32  
    print("%5s  |%5s" % (t,tf))
    t = t + 10