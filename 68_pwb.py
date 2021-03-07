#compute a grade point average

letter_grade = input("Enter all the first letter grade: ")
letter_grade = letter_grade.upper()
count = 0
total_point = 0

while letter_grade != "":
    if letter_grade == "A" or letter_grade == "A+":
        point = 4.0
    elif letter_grade == "A-":
        point = 3.7
    elif letter_grade == "B+":
        point = 3.3
    elif letter_grade == "B":
        point = 3.0
    elif letter_grade == "B-":
        point = 2.7
    elif letter_grade == "C+":
        point = 2.3
    elif letter_grade == "C":
        point = 2.0
    elif letter_grade == "C-":
        point = 1.7
    elif letter_grade == "D+":
        point = 1.3
    elif letter_grade == "D":
        point = 1.0
    elif letter_grade == "F":
        point = 0
    total_point = total_point + point
    count = count + 1
    letter_grade = input("Enter the next letter grade (blank to quit): ")
    letter_grade = letter_grade.upper()

average = total_point / count
print ("The average of the grades you submitted is: ", average)