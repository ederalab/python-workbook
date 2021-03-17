#grade points to letter grade
point = float(input("Enter the point: "))

if point > 4.0:
    letter_grade = "A+"
elif point > 3.7 and point <= 4.0:
    letter_grade = "A"
elif point > 3.3 and point <= 3.7:
    letter_grade = "A-"
elif point > 3.0 and point <= 3.3:
    letter_grade = "B+"
elif point > 2.7 and point <= 3.0:
    letter_grade = "B"
elif point > 2.3 and point <= 2.7:
    letter_grade = "B-"
elif point > 2.0 and point <= 2.3:
    letter_grade = "C+"
elif point > 1.7 and point <= 2.0:
    letter_grade = "C"
elif point > 1.3 and point <= 1.7:
    letter_grade = "C-"
elif point > 1.0 and point <= 1.3:
    letter_grade = "D+"
elif point > 0 and point <= 1.0:
    letter_grade = "D"
elif point == 0:
    letter_grade = "F"

print("The letter grade corresponding to",point,"poiunts is:",letter_grade)
