#gregorian date to ordinal date

def leapYear(year):
    # check if it it a leap year
    divisible_400 = year % 400
    divisible_100 = divisible_400 % 100
    divisible_4 = divisible_100 % 4
    if divisible_400 == 0:
        return True
    elif divisible_100 == 0:
        return False
    elif divisible_4 == 0:
        total = 366
        return True
    else:
        return False

def ordinalDate(day,month,year):
    date = 0
    leap = leapYear(year)
    # add the number of days for each month until the program reaches the month entered by the user
    m = 1
    while m <= month:
        if m == 4 or m == 6 or m == 9 or m == 11:
            date = date + 30
            d = 30 - day
        if m == 2 and leap == True:
            date = date + 29
            d = 29 - day
        if m == 2 and leap == False:
            date = date + 28
            d = 28 - day
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            date = date + 31
            d = 31 - day
        m += 1

    # from the total of days subtract the day entered by the user so I don't add the total number of days in the month entered by the user    
    ordinal_date = date - d
    return ordinal_date

def main():
    day = int(input("Insert the day: "))
    month = int(input("Insert the month: "))
    year = int(input("Insert the year: "))

    ordinal_date = ordinalDate(day,month,year)

    print("The ordinal date is",ordinal_date)

if __name__ == "__main__":
    main()