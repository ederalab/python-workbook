#is a number prime?

def isPrime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    num = int(input("Insert an integer number: "))
    if isPrime(num) == True:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

if __name__ == "__main__":
    main()