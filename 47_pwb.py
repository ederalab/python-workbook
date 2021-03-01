#season from month and day

month = input("Insert the month: ")
month = str.lower(month)
day = int(input("Inser the day: "))

if month == "march":
    if day >= 20:
        season = "spring"
    else:
        season = "winter"
elif month== "april" or month=="may":
        season = "spring"
elif month == "june":
    if day >= 21:
        season = "summer"
    else:
        season = "spring"
elif month == "july" or month=="august":
        season = "summer"
elif month == "september":
    if day >= 22:
        season = "fall"
    else:
        season = "summer"
elif month == "october" or month =="november":
    season = "fall"
elif month == "december":
    if day >= 21:
        season = "winter"
    else:
        season = "fall"
elif month == "january" or month =="february":
    season = "winter"

print(day,month, "is in", season)
