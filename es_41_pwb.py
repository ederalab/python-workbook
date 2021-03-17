#classifying triangles
first_side = float(input("insert the lenght of the first side: "))
second_side = float(input("insert the lenght of the second side: "))
third_side = float(input("insert the lenght of the third side: "))
if first_side == second_side and first_side == third_side:
    print("equilateral")
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("isosceles")
else:
    print("scalene")
