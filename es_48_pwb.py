#birth date to astrological sign

month = input("Insert the month: ")
month = str.lower(month)
day = int(input("Insert the day: "))

if (month=="december" and day >= 22) or (month == "january" and day <= 20):
    sign = "capricorn"
elif (month == "january" and day >= 20) or (month=="february" and day <= 18):
    sign = "acquarius"
elif (month == "february" and day >= 19) or (month=="march" and day <= 20):
    sign = "pisces"
elif (month == "march" and day >= 21) or (month=="april" and day <= 19):
    sign = "aries"
elif (month == "april" and day >= 20) or (month=="may" and day <= 20):
    sign = "taurus"
elif (month == "may" and day >= 21) or (month=="june" and day <= 20):
    sign = "gemini"
elif (month == "june" and day >= 21) or (month=="july" and day <= 22):
    sign = "cancer"
elif (month == "july" and day >= 23) or (month=="august" and day <= 22):
    sign = "leo"
elif (month == "august" and day >= 23) or (month=="september" and day <= 22):
    sign = "virgo"
elif (month == "september" and day >= 23) or (month=="october" and day <= 22):
    sign = "libra"
elif (month == "october" and day >= 23) or (month=="november" and day <= 21):
    sign = "scorpio"
elif (month == "november" and day >= 22) or (month=="december" and day <= 21):
    sign = "sagittarius"

print("Since you're born on",day,month, "your astrological sign is", sign)
