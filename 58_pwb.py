#is it a leap year?

year = int(input("Enter the year to know if it's leap or not: "))

divisible_400 = year % 400
divisible_100 = divisible_400 % 100
divisible_4 = divisible_100 % 4

leap = "is a leap year"
not_leap = "is not a leap year"

if divisible_400 == 0:
    print(year,leap)
elif divisible_100 == 0:
    print(year,not_leap)
elif divisible_4 == 0:
    print(year,leap)
else:
    print(year,not_leap)
