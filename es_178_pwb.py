# recursive palindrome

def palindrome(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] not in alphabet:
        s = s[1:]
        return palindrome(s)
    if s[len(s) - 1] not in alphabet:
        s = s[:-1]
        return palindrome(s)
    if s[0] == s[len(s) - 1]:
        s = s[1 : -1]
        return palindrome(s)

    return False

def main():
    user_string = input("Insert the string and check if is a palindrome ")
    if palindrome(user_string) == True:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")



if __name__ == '__main__':
    main()

