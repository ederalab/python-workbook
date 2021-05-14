# recursive square root
from random import randint

def square_root(n, guess = 1.0):
    if abs((guess**2) - n) < 10** (-12) * n :
        return guess
    else:
        guess = (guess + n/guess)/2
        return square_root(n, guess)


def main():
    n = random.randint(1, 1000)
    print("The square root of",n,"is",square_root(n))


if __name__ == '__main__':
    main()

