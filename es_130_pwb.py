# unary and binary operators

from es_129_pwb import tokenizingString

def checkOperator(t):
    operators = ["+", "-"]
    check = ["*", "/", "+", "-", "^", "{", "[", "(", "="]

    if t[0] in operators:
        if t[0] == "+":
            t[0] = "u+"
        else:
            t[0] = "u-"
    i = 1
    while i < len(t):
        if t[i] in operators:
            if t[i-1] in check:
                if t[i] == "+":
                    t[i] = "u+"
                else:
                    t[i] = "u-"
        i += 1

    return t

def main():
    user_string = input("Insert a mathematical expression and I'll tell you if the + and - operators are unary or not:\n")
    token = tokenizingString(user_string)
    result = checkOperator(token)
    print(result)


if __name__ == '__main__':
    main()