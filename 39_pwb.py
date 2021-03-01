#month name to number of days
month = input("Insert the month: ")
month = str.lower(month)
#30 nov apr giu set
if month == "april" or month == "june" or month == "september" or month == "november":
    print(month,"has 30 days")
elif month == "february":
    print(month,"has 28 or 29 days")
else:
    print(month,"has 31 days")
