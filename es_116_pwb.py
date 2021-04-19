#perfect numbers

from es_115_pwb import properDivisors


def perfectNumber(n):
    t = properDivisors(n)
    if sum(t) == n:
        return True
    else:
        return False


def main():
   for i in range(1, 10001):
       if perfectNumber(i) == True:
           print(i)


main()
