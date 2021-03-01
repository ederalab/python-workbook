#vowel or consonant
insert = input("Insert a letter: ")
letter = str.lower(insert)

if letter == "a" or letter == "e" or letter == "i" or letter =="o" or letter=="u":
    print("The letter",letter,"is a vowel")
elif letter == "y":
    print("Sometimes y is a vowel and sometimes is a consonant")
else:
    print("The letter",letter,"is a consonant")

