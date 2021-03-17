#the collatz conjecture
n = int(input("Insert a positive integer: "))

while n > 0:
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n*3) + 1
        print(n)
    n = int(input("Insert a positive integer: "))
