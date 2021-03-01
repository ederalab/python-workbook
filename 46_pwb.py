#what color is the square?
position = input("Insert the position: ")
position = str.lower(position)
column = position[0]
row = int(position[1])

if column == "a" or column == "c" or column == "e" or column == "g":
    if row % 2 == 0:
        print ("white")
    else:
        print ("black")   
else:
    print ("white")
