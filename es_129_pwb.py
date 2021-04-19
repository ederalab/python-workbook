# tokenizing a string

def tokenizingString(s):
    delimiters = ["*", "/", "+", "-", "^", "{", "}", "[", "]", "(", ")", "="]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #delete all the white spaces
    s = s.replace(" ", "")
    t = []
    i = 0

    while i < len(s):
        #check if the item is a symbol or a number
        if s[i] in delimiters:
            t.append(s[i])
            i += 1
        #check if there are consecutive integers
        elif s[i] in numbers:
            n = ""
            while i < len(s) and s[i] in numbers:
                n = n + s[i]
                i += 1
            t.append(n)
        #check if there are other characters
        else:
            t.append(s[i])
            i += 1

    return t


def main():
    user_string = input("Insert a mathematical expression: ")
    token = tokenizingString(user_string)
    print("The tokens from your list are: ")
    print(token)


if __name__ == '__main__':
    main()



