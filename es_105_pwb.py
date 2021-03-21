#arbitrary base conversions

from es_104_pwb import *

def n2dec(num, base):
    decimal = 0
    for i in range(len(num)):
        decimal = decimal * base
        decimal = decimal + hex2int(num[i])
    return decimal


def dec2n(num,base):
    result = ""
    q = num
    r = q % base
    result = int2hex(r) + result
    q = q // base
    while q > 0:
        r = q % base
        result = int2hex(r) + result
        q = q // base
    return result

def main():
    base = int(input("insert the base to convert from (2 - 16): "))
    if base < 2 or base > 16:
        print("You insert a base outside the range")
        quit()
    num = input("insert the numbers in that base : ")
    dec = n2dec(num,base)
    print("the number is %d in base 10" % dec)

    to_base = int(input("insert the base to convert to (2 - 16): "))
    if to_base < 2 or to_base > 16:
        print("You insert a base outside the range")
        quit()
    to_num = int(dec2n(dec, to_base))
    print("the number is %d in base %d" % (to_num,to_base))


main()