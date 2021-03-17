#median of three values

def median_1(a,b,c):
    if a >= b:
        if b >= c:
            return b
        else:
            return c
    else: #b maggiore di a
        if a >= c:
            return a
        else:
            return b

def median_2(a,b,c):
    max_val = max(a,b,c)
    min_val = min(a,b,c)
    med_val = a + b + c - min_val - max_val
    return med_val

def main():
    a = int(input("Insert the first number: "))
    b = int(input("Insert the second number: "))
    c = int(input("Insert the last number: "))
    med_val = median_1(a,b,c)
    print("The median vaue is",med_val)

main()

