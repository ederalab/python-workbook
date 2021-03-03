#wavelenghts of visible light
wavelenght =  int(input("Enter the wavelenght: "))

if wavelenght >= 380 and wavelenght <450:
    print("violet")
elif wavelenght >= 450 and wavelenght <495:
    print("blue")
elif wavelenght >= 495 and wavelenght <570:
    print("green")
elif wavelenght >= 570 and wavelenght <590:
    print("yellow")
elif wavelenght >= 590 and wavelenght <620:
    print("orange")
elif wavelenght >= 620 and wavelenght <=750:
    print("red")
else:
    print("The wavelenght you entered is outside the visible spectrum")