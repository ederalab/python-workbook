#next day

year = int(input("Insert the year: "))
month = int(input("Insert the month: "))
day = int(input("Insert the day: "))

divisible_400 = year % 400
divisible_100 = divisible_400 % 100
divisible_4 = divisible_100 % 4

next_year = year
next_month = month
next_day = day + 1

if month > 12 or day > 31 or month <= 0 or day <= 0 or (month == 2 and day > 29):
    print ("You entered invalid data")
elif month == 2:
    if day == 28:
        if divisible_400 == 0:
            next_day = day + 1
        elif divisible_100 == 0:
            next_month = month + 1
            next_day = 1
        elif divisible_4 == 0:
            next_day = day + 1
        else:
            next_month = month + 1
            next_day = 1
    elif day == 29:
        if divisible_400 == 0:
            next_month = month + 1
            next_day = 1
        elif divisible_100 == 0:
            print ("The year is not leap")
        elif divisible_4 == 0:
            next_month = month + 1
            next_day = 1
        else:
            print ("The year is not leap")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day > 30: 
        print ("You entered invalid data")
    elif day == 30:
        next_month = month + 1
        next_day = 1
elif month == 12 and day == 31:
    next_month = 1
    next_day = 1
    next_year = year + 1

if len(str(next_month)) == 1:
    next_month = "0" + str(next_month)
if len(str(next_day)) == 1:
    next_day = "0" + str(next_day)

print(next_year,"-",next_month,"-",next_day)
