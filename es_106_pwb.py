#days in a month

def isLeap(year):
    divisible_400 = year % 400
    divisible_100 = divisible_400 % 100
    divisible_4 = divisible_100 % 4

    if divisible_400 == 0:
        return True
    elif divisible_100 == 0:
        return False
    elif divisible_4 == 0:
        return True
    else:
        return False


def daysInMonth(month,year):
    if month <= 0 or month > 12:
        print("You insert an invalid date")
        quit()
    if len(str(year))!= 4:
        print("You insert an invalid date")
        quit()
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeap(year) == True:
            return 29
        else:
            return 28
    else:
        return 31


def main():
    month = int(input("insert the month: "))
    year = int(input("insert the year: "))
    result = daysInMonth(month,year)
    month = str(month).zfill(2)
    print("There are",result,"days in", month,year)

if __name__ == '__main__':
    main()
