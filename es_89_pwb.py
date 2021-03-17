#convert an integer to its ordinal number
def ordinal(n):
    if n >= 1 and n<= 12:
        if n == 1:
            return "first"
        elif n == 2:
            return "second"
        elif n == 3:
            return "third"
        elif n == 4:
            return "fourth"
        elif n == 5:
            return "fifth"
        elif n == 6:
            return "sixth"
        elif n == 7:
            return "seventh"
        elif n == 8:
            return "eighth"
        elif n == 9:
            return "ninth"
        elif n == 10:
            return "tenth"
        elif n == 11:
            return "eleventh"
        elif n == 12:
            return "twelfth"
    else:
        return ""

def main():
    num = int(input("Enter the number:"))
    my_ordinal = ordinal(num)
    print("Number:",num,my_ordinal)

if __name__ == "__main__":
    main()