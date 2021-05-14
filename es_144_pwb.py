# anagrams again

from es_143_pwb import anagrams

def check(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2. replace(" ", "")

    s1 = s1.upper()
    s2 = s2.upper()

    if anagrams(s1) == anagrams(s2):
        return True
    else:
        return False


def main():
    s1 = input("Insert the first string\n")
    s2 = input("Insert the second string\n")
    r = ""
    if check(s1,s2) == False:
        r = "not "
    print(f"The strings '{s1}' and '{s2}' are {r}anagrams")


if __name__ == '__main__':
    main()
