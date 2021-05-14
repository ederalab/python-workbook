# postal codes

def canadian_postal_codes(code):
    code = code.upper()
    code = code.replace(" ","")
    province = {"A": "Newfoundland", "B":"Nova Scotia", "C":"Prince Edward Island", "E":"New Brunswick", "G":"Quebec", "H":"Quebec", "J":"Quebec", "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario", "R":"Manitoba", "S":"Saskatchewan", "T":"Alberta", "V":"British Columbia", "X":"Nunavut", "X":"Northwest Territories", "Y":"Yukon"}
    error = "Error! The postal code is not valid"
    if len(code) != 6 or code[0] not in province or code[1].isdigit() == False or code[2].isdigit() == True:
        return error, ""

    area = province[code[0]]
    if code[1] == "0":
        type = "rural"
    else:
        type = "urban"

    return area, type


def main():
    user_string = input("Insert the postal code: ")
    area, type =  canadian_postal_codes(user_string)
    n= ""
    if type == "urban":
        n = "n"

    print(f'This is a{n} {type} address in {area}')

if __name__ == '__main__':
    main()
