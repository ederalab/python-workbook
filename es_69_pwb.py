#admission price
total_charge = 0.00
age_baby = 2
age_child = 12
age_senior = 65
charge_baby = 0.00
charge_child = 14.00
charge_senior = 18.00
charge_standard = 23.00

guest_age = input ("Enter the age of each guest (blank if there are no more guests): ")

while guest_age != "":
    guest_age = int(guest_age)
    if guest_age <= age_baby:
        total_charge += charge_baby
    elif guest_age >= age_baby+1 and guest_age <= age_child:
        total_charge += charge_child
    elif guest_age >= age_senior:
        total_charge += charge_senior
    else:
        total_charge += charge_standard
    guest_age = input ("Enter the age of each guest (blank if there are no more guests): ")

print("The admission cost for the group is %.2f$" % total_charge)
