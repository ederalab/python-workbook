#does a string represent an integer?
def isInteger(s):
    s = s.strip()
    if len(s)<1:
        return False
    if (s[0]=="+" or s[0]=="-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

def main():
    s = input("Insert the string: ")
    result = isInteger(s)
    if result == True:
        print("The string is integer")
    else:
        print("The string is not integer")

if __name__==("__main__"):
    main()