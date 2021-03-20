#random good password
"""
write a program that generates a random good pasw
count and display the num of attempts needed before it is generated
"""

from es_100_pwb import randomPassword
from es_102_pwb import checkPassword

def goodRandomPassword():
    attempts = 1
    loop = True
    while loop != False:
        password = randomPassword()    
        check_pass = checkPassword(password)
        if check_pass == True:
            loop = False
            return password, attempts
        else:
            attempts += 1            

def main():
    password, attempts = goodRandomPassword()
    print("The good password generated randomly is", password)
    print("It took",attempts,"attempts to get it")

if __name__ == "__main__":
    main()

