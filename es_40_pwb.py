#sound levels
decibel = int(input("Insert the number of decibel: "))
if decibel > 130:
    print(decibel, "DB is louder than the Jackhammer noise")
elif decibel == 130:
    print(decibel, "DB is the Jackhammer noise")
elif decibel < 130 and decibel > 106:
    print(decibel, "DB is between the Jackhammer and the Gas Lawnmower noise")
elif decibel == 106:
    print(decibel, "DB is the Gas Lawnmower noise")
elif decibel < 106 and decibel > 70:
    print(decibel, "DB is between the Gas Lawnmower and the Alarm Clock noise")
elif decibel == 70:
    print(decibel, "DB is the Alarm Clock noise")
elif decibel < 70 and decibel > 40:
    print(decibel, "DB is between the Alarm Clock and the Quiet Room noise")
elif decibel == 40:
    print(decibel, "DB is the Quiet Room noise")
elif decibel < 40:
    print(decibel, "DB is lower then the Quiet Room noise")
