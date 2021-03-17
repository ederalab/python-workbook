#random password
import random

def randomPassword():
    i = 0
    n = random.randint(7,10)
    mypass = ""
    while i < n:
        c = random.randint(33,126)
        mypass = mypass + chr(c)
        i += 1
    return mypass

def main():
    mypass = randomPassword()
    print("The randomly generated password is",mypass)

if __name__ == "__main__":
    main()
