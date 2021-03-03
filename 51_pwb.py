#roots of a quadratic function
a = float(input("insert the value of the constant a: "))
b = float(input("insert the value of the constant b: "))
c = float(input("insert the value of the constant c: "))

discriminant = (b**2) - (4 * a * c)

if discriminant < 0:
    print("the quadratic equation doesn't have any real root")
elif discriminant == 0:
    root = -b / 2*a
    print("the quadratic equation has one real root:", root)
else:
    root1 = (-b+discriminant) / 2*a
    root2 = (-b-discriminant) / 2*a
    print("the quadratic equation has two real roots:",root1,"and",root2)

