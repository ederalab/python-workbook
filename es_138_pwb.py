# text messaging

def keypad_dictionary(s):
    keypad = {1 : [".", ",","?","!",":"], 2 : ["A", "B", "C"], 3 : ["D", "E", "F"], 4 : ["G", "H", "I"], 5 : ["J", "K", "L"], 6 : ["M", "N", "O"], 7 : ["P", "Q", "R", "S"], 8 : ["T", "U", "V"], 9 : ["W", "X", "Y", "Z"], 0 : " "}
    mapkeypad = {}
    for k in keypad:
        val = keypad[k]
        count = 1
        for i in val:
            mapkeypad[i] = count * str(k)
            count += 1

    s = s.upper()
    result = ""

    for c in s:
        n = mapkeypad[c]
        result = result + n

    return result


def main():
    user_string = input("Insert your string: ")
    result = keypad_dictionary(user_string)
    print("If you want to write it with an old phone you have to digit these numbers")
    print(result)


if __name__ == '__main__':
    main()