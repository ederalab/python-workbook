#word by word palindromes

from es_117_pwb import onlyWords

def wordByWord(s):
    s = s.lower()
    t = onlyWords(s)
    i = 0
    j = len(t) - 1

    while i < len(t):
        result = True
        if t[i] != t[j]:
            result = False
        i += 1
        j -= 1

    return result

def main():
    user_string = input("Insert a string and I'll check if it is palindrome \n")
    if wordByWord(user_string) == True:
        print("Yes, the string is palindrome")
    else:
        print("The string is not palindrome")


if __name__ == "__main__":
    main()
