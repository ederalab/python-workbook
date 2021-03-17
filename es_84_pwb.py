#coin flip simulation
"""
minimum number of times you have to flip a coin before having 3 consecutive flips with the same outcome
maximum ?
use random number generator to simulate the flipping several times
H - T
number to obtain 3 consecutive
10 times simulation
report the average
"""
import random

flips = 0
consec = 1
coins = ("H", "T")
last =""
i = 0
j = 1
total_flips = 0
while j != 0 :
    coin = random.choice(coins)
    if j == 1:
        last = coin
        flips = flips + 1
        i = i + 1
        print(coin, end = " ")
    else:
        if coin == last:
            consec = consec + 1
            print(coin, end = " ")
        else:
            last = coin
            consec = 1
            print(coin, end = " ")
        flips = flips + 1
        if consec == 3:
            print("(%d flips)" % flips)
            i = i + 1
            flips = 0
            consec = 0
    j += 1
    total_flips += 1
    if i == 10:
        j=0

average = total_flips / 10
print("On average,",average,"flips were needed")