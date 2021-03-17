#making change
#reading the int number of cents from the user 
#compute and display the denomination of the coins to give the amount of change
"""
penny = 0.01 $
nickel = 0.05 $
dime = 0.1 $
quarter = 0.25 $ 
loony = 1 $
toony = 2 $
"""

cents = int(input("Insert coins: "))

pennies = 1
nickels = 5
dimes = 10
quarters = 25
loonies = 100
toonies = 200

n_toonies = cents // toonies
print("", n_toonies, "toonies")
cents = cents % toonies

n_loonies = cents // loonies
print("", n_loonies, "loonies")
cents = cents % loonies

n_quarters = cents // quarters
print("", n_quarters, "quarters")
cents = cents % quarters

n_dimes = cents // dimes
print("", n_dimes, "dimes")
cents = cents % dimes

n_nickels = cents // nickels
print("", n_nickels, "nickels")
cents = cents % nickels

n_pennies = cents // pennies
print("", n_pennies, "pennies")
cents = cents % pennies
