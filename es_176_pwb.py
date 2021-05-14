# the NATO phonetic alphabet

def phonetic_alphabet(s, r):
    d = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu"
    }
    result = r

    if s == "" and result == "":
        return "You entered an empty string"
    else:
        s = s.upper()
        if "A" <= s[0] <= "Z":
            result += d[s[0]] + " "
        if s[1:] != "":
            return phonetic_alphabet(s[1:], result)
        else:
            return result


def main():
    user_string = input("Please enter a string to convert in NATO Phonetic Alphabet:\n ")
    print(phonetic_alphabet(user_string, ""))


if __name__ == '__main__':
    main()
