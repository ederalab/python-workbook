#sort 3 integers
a = int(input("Type the first integer number: "))
b = int(input("Type the second integer number: "))
c = int(input("Type the last integer number: "))

the_min = min(a,b,c)
the_max = max(a,b,c)
the_sum = a + b + c
the_mid = the_sum - the_min - the_max

print("The order of the numbers is, from smallest to largest:\n", the_min, "\n", the_mid, "\n", the_max)
