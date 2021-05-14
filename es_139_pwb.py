# morse code
def morse_code(s):
    code = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----."}
    s = s.upper()
    result = ""
    for c in s:
        if c not in code:
            result = result + ""
        else:
            result = result + code[c] + " "
    return result


def main():
    user_string = input("Insert your secret string to transfer with morse code: ")

if __name__ == '__main__':
    main()
