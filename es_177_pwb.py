# roman numerals

def roman_numerals(num, res):
    d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    if num == "":
        return res
    else:
        if len(num) == 1 or d[num[0]] >= d[num[1]]:
            res += d[num[0]]
        else:
            res -= d[num[0]]

        num = num[1:]
        return roman_numerals(num, res)


def main():
    user_string = input("Please enter a roman number ")
    print(roman_numerals(user_string, 0))


if __name__ == '__main__':
    main()
