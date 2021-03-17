#random license plate
import random, string

def licensePlate():
    plate_type = random.choice(["old","new"])
    l = 0
    d = 0
    plate = ""
    
    if plate_type == "old":
        while l < 3:
            plate = plate + random.choice(string.ascii_uppercase)
            l += 1
        while d < 3:
            plate = plate + str(random.randint(0,9))
            d = d+1
        return plate
    else:
        while d < 4:
            plate = plate + str(random.randint(0,9))
            d = d+1
        while l < 3:
            plate = plate + random.choice(string.ascii_uppercase)
            l += 1
        return plate

def main():
    my_plate = licensePlate()
    print("The random plate is", my_plate)

if __name__ == "__main__":
    main()