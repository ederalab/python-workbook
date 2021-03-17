#capitalize it
"""

    #result = quote.find('let it')
    #print("Substring 'let it':", result)
"""

def capitalizeIt(s):
    #capitalize the first non-space character in the string
    i = 0
    mystring = s
    while i < len(s) and mystring[i] == " ":
        i = i+1
    if i < len(s):
        #take the substring from 0 to i + first letter to be capitalized + substring from the next letter until the end
        mystring = mystring[0 : i] + mystring[i].upper() + mystring[i + 1:len(mystring)]

    #capitalize the first non-space character after a period, exclamation mark or question mark
    i = 0
    while i < len(s):
        if mystring[i]== "!" or mystring[i]=="?" or mystring[i]==".":
            i = i+1
            while i < len(s) and mystring[i] == " ":
                i = i+1
            if i < len(s):
                mystring = mystring[0 : i] + mystring[i].upper() + mystring[i + 1:len(mystring)]
        i = i+1
    
    #capitalize a lowercase i if it is preceded by a space and followed by a space, period, exclamation mark, question mark or apostrophe 
    i = 1
    while i < len(s) - 1:
        if (mystring[i-1]==" " or mystring[i-1]=="." or mystring[i-1]=="!" or mystring[i-1]=="?" or mystring[i-1]=="'") and mystring[i]=="i" and (mystring[i+1]==" " or mystring[i+1]=="." or mystring[i+1]=="!" or mystring[i+1]=="?" or mystring[i+1]=="'"):
            mystring = mystring[0 : i] + mystring[i].upper() + mystring[i + 1:len(mystring)]
        i = i+1
    
    return(mystring)

def main():
    s = input("Enter the string: ")
    capitalize_string = capitalizeIt(s)
    print(capitalize_string)

main()