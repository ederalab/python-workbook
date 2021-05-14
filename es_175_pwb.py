# recursive decimal to binary

def dec2bin(n):
    result = ''
    if n == 0:
        return 0
    if n == 1:
        result = str(1) + result
        return result
    elif n > 0:
        r = n % 2
        result = str(r) + result
        n = n // 2
        return dec2bin(n) + result
    else:
        return 'Error: please insert a positive number'


def main():
    try:
        number = int(input("Please insert a positive number and I'll convert it into binary: "))
        print(dec2bin(number))
    except:
        print("Not valid number!")
        quit

if __name__ == '__main__' :
    main()