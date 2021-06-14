# evaluate postfix

from es_129_pwb import tokenizingString
from es_130_pwb import checkOperator
from es_131_pwb import infixToPostfix
from es_96_pwb import isInteger

def evaluatePostfix(postfix):
    values = []

    for token in postfix:
        if isInteger(token) == True:
            token = int(token)
            values.append(token)
        elif token == "u-":
            x = values.pop(len(values) - 1)
            x = "-" + str(x)
            values.append(x)
        elif token == "+" or "-" or "*" or "/" or "^":
            right = values.pop(len(values) - 1)
            left = values.pop(len(values) - 1)
            """
            x = int(left) + token + int(right)
            #x = "left" + token + "right"
            #values.append(eval(x))
            eval('%d %s %d' % (left, symbol, right)
            """
    #return values[0]





def main():
    #s = input("Insert a mathematical expression: ")
    s = "12 + 45 - (-3 / 2)"
    t = tokenizingString(s)
    infix = checkOperator(t)
    postfix = infixToPostfix(infix)
    # print(postfix)
    result = evaluatePostfix(postfix)
    #print(result)


if __name__ == '__main__':
    main()

