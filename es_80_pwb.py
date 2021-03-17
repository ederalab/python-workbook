#prime factors
n = int(input("Enter an integer (2 or greater):"))
f = 2
if n < 2:
    print("The number you submitted is not greater than 2")
    n = int(input("Please enter again (2 or greater):"))
else:
    print("The prime factors of",n,"are:")
    while f <= n:
        if n % f == 0:
            print (f)
            n = n // f
        else:
            f = f+1


