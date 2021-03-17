#square root
from math import sqrt
x = float(input("Insert the number: "))
guess = x/2

square_root = sqrt(x)
print('square root of %.2f is %.4f' % (x, square_root))

while abs((guess**2) - x) > 10**-12:
    guess = (guess + x/guess) / 2

print('square root of %.2f is %.4f' % (x, guess))
