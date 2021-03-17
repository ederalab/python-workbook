#roulette payouts
from random import randrange
number = randrange(0,37)

black = 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
red = 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
if number == 37:
    number == "00"

if number in black:
    pay01 = "Black"
else:
    pay01 = "Red"

if number % 2 == 0 and number != 0:
    pay02 = "Even"
elif number % 2 != 0 and number != 37:
    pay02 = "Odd"

if number>= 1 and number <= 18:
    pay03 = "1 to 18"
elif number >=19 and number <= 36:
    pay03 = "19 to 36"

print("The spin resulted in",number,"...")
print("Pay",pay01)
print("Pay",pay02)
print("Pay",pay03)
