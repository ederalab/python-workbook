#chinese zodiac

year = int(input("Insert the year: "))
rest = (year - 2000) % 12

if rest == 0:
    zodiac = "Dragon"
elif rest == 1:
    zodiac = "Snake"
elif rest == 2:
    zodiac = "Horse"
elif rest == 3:
    zodiac = "Sheep"
elif rest == 4:
    zodiac = "Monkey"
elif rest == 5:
    zodiac = "Rooster"
elif rest == 6:
    zodiac = "Dog"
elif rest == 7:
    zodiac = "Pig"
elif rest == 8:
    zodiac = "Rat"
elif rest == 9:
    zodiac = "Ox"
elif rest == 10:
    zodiac = "Tiger"
elif rest == 11:
    zodiac = "Hare"

print(year, "is the year of", zodiac)
