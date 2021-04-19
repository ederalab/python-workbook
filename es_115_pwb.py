#list of proper divisors

def properDivisors(n):
    t = []
    i = 1
    while i < n:
        if n % i == 0:
            t.append(i)
        i += 1
    return t

def main():
    n = int(input("Insert an integer number (blank to quit): "))
    print (properDivisors(n))


if __name__ == "__main__":
    main()
