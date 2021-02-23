#sum of the digits in an integer
number = int(input("Insert a 4 digit number: "))
numstr = str(number)
i = 0
count = 0
n = len(numstr)
printnum = " "

while i <= n :
    if i != n :
        count = count + int(numstr[i])
        printnum += numstr[i] + " + "
    else :
        count = str(count)
        printnum = printnum + " = " + count
    i = i+1

print(printnum)