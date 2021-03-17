#compute the hypotenuse
from math import sqrt
def my_hyp (a,b):
    c = (a**2)+(b**2)
    c = sqrt(c)
    return c

def main():
    side_1 = float(input("Enter the lenght of side 1:"))
    side_2 = float(input("Enter the lenght of side 2:"))

    hyp = my_hyp(side_1,side_2)
    print(hyp)

main()