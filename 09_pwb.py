#compound interest
#earns 4% per year 
#amount in the savings account after 1/2/3 years - 2 decimal

amount = float(input("Insert the initial amount of your account: "))
year = 0
while year < 3 : 
    earns = amount * 4 / 100
    year = year + 1
    print("the earn this year is: %.2f " % earns)
    amount = amount + earns 

    if year == 1:
        the_year = str(year) + "st"
    elif year == 2:
        the_year = str(year) + "nd"
    elif year == 3:
        the_year = str(year) + "rd"
    else :
        the_year = str(year) + "th"

    print("the amount at the end of the", the_year, "year is: %.2f " % amount)

print ("the total amount after earning the interests is: %.2f " % amount)