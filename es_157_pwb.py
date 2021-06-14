# Both Letter Grades and Grade Points

def pointsToLetterGrade(point):
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

    return letter_grade

def letterGradeToPoint(letter_grade):
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

    return point


def main():
    letter_grades = ['A+', 'A-', 'A', 'B+', 'B-', 'B', 'C+', 'C-', 'C', 'D+', 'D', 'F']

    user_value = input('Enter a point or a letter grade to convert (blank line to quit): ')

    while user_value != "":
        try:
            if user_value in letter_grades:
                ltp = letterGradeToPoint(user_value.upper())
                print(user_value, 'is equals to', ltp)
            else:
                ptl = pointsToLetterGrade(float(user_value))
                print(user_value, 'is equals to', ptl)
        except:
            print('Please enter a correct point or letter grade')

        user_value = input('Enter a point or a letter grade to convert (blank line to quit): ')


if __name__ == '__main__':
    main()
