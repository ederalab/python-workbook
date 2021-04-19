#magic dates
from es_106_pwb import *

#check if is a magic date
def magicDate(d,m,y):
    y = str(y)
    y = y[2]+y[3]
    y = int(y)
    if d * m == y:
        return True
    return False
def main():
    result=""
    for year in range(1900,2000):
        for month in range (1,13):
            for day in range (1, daysInMonth(month,year) + 1):
                if magicDate(day,month,year):
                    #if it's a magic date add to the result string
                    result = result + str(day).zfill(2) + "-" + str(month).zfill(2) + "-" + str(year) + "\n"
    print("Magic dates in 1900s are:")
    print(result)

main()