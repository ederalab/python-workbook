#Area of a Field
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
sqft_per_acre = 43560
area = width * height / sqft_per_acre
print('The area of the field is: ', area, ' acres')
