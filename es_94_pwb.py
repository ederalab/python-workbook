#is it a valid triangle?

def triangle(a,b,c):
    #check if any length is equal or less than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        max_length = max(a,b,c)
        sum_length = a + b + c - max_length
        #check if one length is greater than the sum of the other two
        if max_length >= sum_length:
            print("The triangle cannot be formed")
        else:
            print("It is a valid triangle!")
        
def main():
    a = int(input("Insert the length of the first side: "))
    b = int(input("Insert the length of the second side: "))
    c = int(input("Insert the length of the third side: "))

    triangle(a,b,c)

main()