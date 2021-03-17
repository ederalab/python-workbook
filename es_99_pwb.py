#next prime
from es_98_pwb import isPrime

def nextPrime(n):
    i = n
    while isPrime(i) == False:
        i = i + 1
    return i

def main():
    n = int(input("Insert an integer: "))
    num = nextPrime(n)
    print("The next prime number after",n,"is",num)

main()