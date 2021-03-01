#faces on money
amount = int(input("Enter the banknote: "))

if amount == 1:
    print("George Washington")
elif amount == 2:
    print("Thomas Jefferson")
elif amount == 5:
    print("Abraham Lincoln")
elif amount == 10:
    print("Alexander Hamilton")
elif amount == 20:
    print("Andrew Jackson")
elif amount == 50:
    print("Ulysses S. Grant")
elif amount == 100:
    print("Benjamin Franklin")
else :
    print("I can't recognize this banknote")
