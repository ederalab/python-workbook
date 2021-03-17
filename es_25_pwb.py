#units of time reverse DD:HH:MM:SS

total = int(input("Insert the number of total seconds: "))
seconds_per_day = 60 * 60 * 24
seconds_per_hour = 60 * 60
seconds_per_minute = 60

days = total // seconds_per_day
total_hours = total % seconds_per_day
hours = total_hours // seconds_per_hour
total_minutes = total_hours % seconds_per_hour
minutes = total_minutes // seconds_per_minute
seconds = total_minutes % seconds_per_minute

print ("%d:%02d:%02d:%02d" %(days,hours,minutes,seconds) )
