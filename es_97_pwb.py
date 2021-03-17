#operator precedence

def precedence(operator):
    operator = operator.strip()
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "**" or operator == "^":
        return 3
    else:
        return -1

def main():
    myoperator = input("Insert the operator: ")
    result = precedence(myoperator)
    if result == -1:
        print("You didn't insert an operator")
    else:
        print("The operator",myoperator,"has precedence",result)

if __name__ == "__main__":
    main()