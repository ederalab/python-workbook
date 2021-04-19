#reduce a fraction to lowest terms

def greatestCommonDivisor(n,m):
    d = min(n, m)
    while (m % d != 0) or (n % d != 0):
        d = d - 1
    return d


def lowestTerms(num,den):
    if num == 0:
        return (0,1)
    gcd = greatestCommonDivisor(num,den)
    lowest_num = num // gcd
    lowest_den = den // gcd
    return (lowest_num, lowest_den)


def main():
    num = int(input("Enter the numerator of the fraction: "))
    den = int(input("Enter the denominator of the fraction: "))
    (lowest_num, lowest_den) = lowestTerms(num,den)
    print(lowest_num, lowest_den)


if __name__ == "__main__":
    main()