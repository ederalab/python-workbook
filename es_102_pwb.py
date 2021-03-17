#check a password
def checkPassword(password):
    check_lower = False
    check_upper = False
    check_digit = False

    for c in password:
        if c >= "a" and c <= "z":
            check_lower = True
        if c >= "A" and c <= "Z":
            check_upper = True
        if c >= "0" and c <= "9":
            check_digit = True
            
    if len(password) >= 8 and check_lower == True and check_upper == True and check_digit == True:
        return True
    else:
        return False
            

def main():
    password = input("Enter the password: ")
    check_pass = checkPassword(password)
    if check_pass == True:
        print ("The password is valid")
    else:
        print ("The password is not valid")
    
if __name__ == "__main__":
    main()