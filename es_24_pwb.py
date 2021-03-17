#units of time
days = int(input("Insert days: "))
hours = int(input("Insert hours: "))
minutes = int(input("Insert minutes: "))
seconds = int(input("Insert the number of seconds: "))

minutes = minutes * 60
hours = hours * 60 * 60
days = days * 24 * 60 * 60

total = days + hours + minutes + seconds

print ("The number of total seconds is: ", total)
