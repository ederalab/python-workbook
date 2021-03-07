#average
value = int(input("Submit the values for the compute: "))
values = 0
n = 0
while value != 0:
    values += value
    value = int(input("Submit the values for the compute: "))
    n = n+1

average = values / n
print(average)