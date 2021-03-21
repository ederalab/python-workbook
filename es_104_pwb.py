# hexadecimal and decimal digits

def hex2int(myhex):
    myhex = myhex.upper()
    if len(myhex) > 6:
        return "This is not an hexadecimal number"
    i = 0
    e = len(myhex) - 1
    result = 0
    #check if the number corresponds to a number or a letter
    while i < len(myhex):
        n = myhex[i]
        if n == "A":
            n = 10
        elif n == "B":
            n = 11
        elif n == "C":
            n = 12
        elif n == "D":
            n = 13
        elif n == "E":
            n = 14
        elif n == "F":
            n = 15
        elif n >"F":
            return "This is not an hexadecimal number"
        else:
            n = int(myhex[i])

        result = result + (n * (16**e))
        i += 1
        e -= 1
    return result

def int2hex(myint):
    # prepare a function to be used different times later to convert number to letter
    def l2n(d):
        if d == 10:
            return "A"
        elif d == 11:
            return "B"
        elif d == 12:
            return "C"
        elif d == 13:
            return "D"
        elif d == 14:
            return "E"
        elif d == 15:
            return "F"
        else:
            return d

    result = ""
    myint = int(myint)
    q = myint // 16
    r = myint % 16
    result = result + str(l2n(r))
    while (q//16) > 0:
        r = q % 16
        result = result + str(l2n(r))
        q = q // 16
    r = q % 16
    result = result + str(l2n(r))
    result = result[::-1]
    return result


def main():
    myhex = input("enter the hexadecimal number to be converted: ")
    result_int = hex2int(myhex)
    print(result_int)
    myint = input("enter the decimal number to be converted: ")
    #check if they are only digits
    if myint.isdigit() == False:
        print("This is not a decimal number")
    else:
        result_hex = int2hex(myint)
        print(result_hex)


if __name__ == "__main__":
    main()