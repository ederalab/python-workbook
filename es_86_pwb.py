#taxi fare
def taxi_fare(d):
    base = 4
    fee = 0.25 #every 140 meters
    #meters
    compute = (d * 1000) // 140
    total = base + (compute * fee)
    return total

def main():
    distance = float(input("Insert the distance in km: "))
    tot = taxi_fare(distance)
    print("The total taxi fare is %.2f$" % tot)

main()