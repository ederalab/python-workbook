#what day of the week is january 1
import math

year = int(input("Enter the year: "))
day_of_the_week = (year + math.floor((year - 1)/4) - math.floor((year-1)/100) + math.floor((year-1)/400)) % 7

if day_of_the_week == 0:
    day = "Sunday"
elif day_of_the_week == 1:
    day = "Monday"
elif day_of_the_week == 2:
    day = "Tuesday"
elif day_of_the_week == 3:
    day = "Wednesday"
elif day_of_the_week == 4:
    day = "Thursday"
elif day_of_the_week == 5:
    day = "Friday"
elif day_of_the_week == 6:
    day = "Saturday"

print("In", year,",the first of January is",day)