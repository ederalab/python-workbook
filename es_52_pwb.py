#letter grade to grade points
letter_grade = input("Enter the letter grade: ")
text_to_print = "The grade point is:"

if letter_grade == "A" or letter_grade == "A+":
    print(text_to_print, 4.0)
elif letter_grade == "A-":
    print(text_to_print, 3.7)
elif letter_grade == "B+":
    print(text_to_print, 3.3)
elif letter_grade == "B":
    print(text_to_print, 3.0)
elif letter_grade == "B-":
    print(text_to_print, 2.7)
elif letter_grade == "C+":
    print(text_to_print, 2.3)
elif letter_grade == "C":
    print(text_to_print, 2.0)
elif letter_grade == "C-":
    print(text_to_print, 1.7)
elif letter_grade == "D+":
    print(text_to_print, 1.3)
elif letter_grade == "D":
    print(text_to_print, 1.0)
elif letter_grade == "F":
    print(text_to_print, 0)
else:
    print("You entered an invalid letter grade")
