#what color is the square?
position = input("Insert the position: ")
position = str.lower(position)
column = position[0]
row = int(position[1])

if (column == "a" or column == "c" or column == "e" or column == "g") and row <= 8:
    if row % 2 == 0:
        print ("white")
    else:
        print ("black")  
elif (column == "b" or column == "d" or column == "f" or column == "h") and row <= 8:
    if row % 2 == 0:
        print ("black")
    else:
        print ("white")  
else:
    print ("You entered a wrong position")
