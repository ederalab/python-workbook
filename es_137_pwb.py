# two dice simulation
from random import randint

def twoDiceSimulation():
    expected_total = {2 : 2.78, 3 : 5.56, 4 : 8.33, 5 : 11.11, 6 : 13.89, 7 : 16.67 , 8 : 13.89, 9 : 11.11, 10 : 8.33, 11 : 5.56, 12 : 2.78}
    total = {2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0 , 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
    simulations = 1000
    for i in range(0, simulations):
        d = randint(1,6) + randint(1,6)
        total[d] = total[d] + 1

    print("Total   Simulated   Expected")
    print("          Percent    Percent")

    for i in sorted(total.keys()):
        simulated = total[i] / simulations * 100
        expected = expected_total[i]
        print("%5d %11.2f %9.2f" % (i, simulated, expected))



twoDiceSimulation()

