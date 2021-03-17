#cell phone bill
air_time = 50
sms = 50
monthly_cost = 15.00
additional_air_time = 0.25
additional_sms = 0.15
support_911 = 0.44
tax_fee = 5 #percent

minutes = int(input("Insert the minute used in a month: "))
messages = int(input("Insert the messages sent in a month: "))

if minutes > 50 or messages > 50:
    extra_minutes_cost = 0
    extra_messages_cost = 0
    if minutes > 50:
        extra_minutes_cost = (minutes - air_time) * additional_air_time
        print("The additional cost for minutes is %.2f" % extra_minutes_cost,"$")
    if messages > 50:
        extra_messages_cost = (messages - sms) * additional_sms
        print("The additional cost for messages is %.2f" % extra_messages_cost,"$")
    subtotal = monthly_cost + support_911 + extra_minutes_cost + extra_messages_cost
    tax = subtotal * tax_fee / 100
    total = subtotal + tax
    print("The subtotal is %.2f" % subtotal,"$")
    print("The tax is %.2f" % tax,"$")
    print("The total of the bill is %.2f" % total,"$")
