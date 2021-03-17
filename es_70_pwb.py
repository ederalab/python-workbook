#parity bits

line = input("Enter a 8 bit string (blank to stop): ")

while line != "":
    if len(line) != 8 or (line.count("0") + line.count("1")) != 8:
        print("This is not a 8 but string")
    else:
        one_count = line.count("1")
        if one_count % 2 == 0:
            print("parity bits 0")
        else:
            print("parity bits 1")
    line = input("Enter a 8 bit string (blank to stop): ")
