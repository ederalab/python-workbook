#ordinal date to gregorian date

from es_91_pwb import leapYear, ordinalDate

def gregorianDate(days,year, l):
    #count days in the month
    jan = 31
    feb = jan + 28 + l
    mar = feb + 31 + l
    apr = mar + 30 + l
    may = apr + 31 + l
    jun = may + 30 + l
    jul = jun + 31 + l
    aug = jul + 31 + l
    sep = aug + 30 + l
    ott = sep + 31 + l
    nov = ott + 30 + l
    dec = nov + 31 + l

    #convert
    if days <= jan: 
        month = "01"
        day = days
    elif days > jan and days <= feb :
        month = "02"
        day = days - jan
    elif days > feb and days <= mar :
        month = "03"
        day = days - feb
    elif days > mar and days <= apr :
        month = "04"
        day = days - mar
    elif days > apr and days <= may :
        month = "05"
        day = days - apr
    elif days > may and days <= jun :
        month = "06"
        day = days - may
    elif days > jun and days <= jul :
        month = "07"
        day = days - jun
    elif days > jul and days <= aug :
        month = "08"
        day = days - jul
    elif days > aug and days <= sep :
        month = "09"
        day = days - aug
    elif days > sep and days <= ott :
        month = "10"
        day = days - sep
    elif days > ott and days <= nov :
        month = "11"
        day = days - ott
    elif days > nov and days <= dec :
        month = "12"
        day = days - nov

    day = str(day)
    if len(day) == 1:
        day="0"+day

    #return multiple values
    return day, month

def returnPeriod(return_period,day,year,l):
    return_day = day + return_period
    tot_year = 365 + l
    if return_day > tot_year:
        year = year + 1
        return_day = return_day - tot_year
        l = leapYear(year)
    day, month = gregorianDate(return_day, year, l)
    return day, month, year


def main():
    insert_date = int(input("Insert the day in ordinal format: "))
    year = int(input("Insert the year: "))
    
    #check if it is leap
    is_leap = leapYear(year)
    if (is_leap == True):
        l = 1
    else:
        l = 0
    
    #check if the number of days are correct
    
    if insert_date > (365 + l):
        print("Invalid date!")
        insert_date = int(input("Insert the day in ordinal format: "))
        year = int(input("Insert the year: "))

    #take 2 values returned
    day,month = gregorianDate(insert_date,year, l)
    #print the data
    print("%2s-%2s-%d" % (day,month,year))

    return_period = int(input("Insert the return days: "))
    return_day,return_month,return_year = returnPeriod(return_period, insert_date, year, l)
    #print the data
    print("The latest day to return the product is %2s-%2s-%d" % (return_day,return_month,return_year))

main()