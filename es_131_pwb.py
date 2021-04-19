# infix to postfix

from es_129_pwb import tokenizingString
from es_130_pwb import checkOperator
from es_96_pwb import isInteger

def precedence(operator):
    operator = operator.strip()
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "u+" or operator == "u-":
        return 3
    elif operator == "**" or operator == "^":
        return 4
    else:
        return -1

def infixToPostfix(infix):
    operator = []
    postfix = []
    op = ["*", "/", "+", "-", "^", "=", "u+", "u-"]

    for token in infix:
        if isInteger(token) == True:
            postfix.append(token)
        elif token in op:
            while operator != [] \
                    and operator[len(operator) - 1] != "(" \
                    and precedence(token) <= precedence(operator[len(operator) - 1]):
                x = operator.pop(len(operator) - 1)
                postfix.append(x)
            operator.append(token)
        elif token == "(":
            operator.append(token)
        elif token == ")":
            while operator[len(operator) - 1] != "(":
                x = operator.pop(len(operator) - 1)
                postfix.append(x)
            operator.remove("(")

    while operator:
        x = operator.pop(len(operator) - 1)
        postfix.append(x)

    return postfix




def main():
    s = input("Insert a mathematical expression: ")
    t = tokenizingString(s)
    infix = checkOperator(t)
    postfix = infixToPostfix(infix)
    print(postfix)


if __name__ == '__main__':
    main()