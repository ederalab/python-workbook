# write out numbers in english 0-999

from random import randint

def num2word(n):
    num = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    max = 1000

    if n < 20:
        return num[n]

    if 20<= n < 100:
        if n % 10 == 0:
            return num[n]
        else:
            return num[n // 10 * 10] + " " + num[n % 10]

    if 100 <= n < max:
        if n % 100 == 0:
            return num[n // 100] + " hundred"
        else:
            return num[n // 100] + " hundred " + str(num2word(n % 100))



def main():
    n = randint(0,999)
    print(n, "equals to", num2word(n))


if __name__ == '__main__':
    main()
