#date to holiday name
month = input("Enter the month: ")
month = str.lower(month)
day = int(input("Enter the day: "))

if month == "january" and day == 1:
    print("It's New Year's Day!")
elif month == "july" and day == 1:
    print("It's Canada Day!")
elif month =="december" and day == 25:
     print("It's Christmas Day!")
else:
    print("This date doesn't correspond to any fixed-date holiday")

