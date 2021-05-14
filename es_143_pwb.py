# anagrams

def anagrams(s):
    d = {}
    i = 1
    for c in s:
        if c not in d:
            d[c] = i
        else:
            d[c] += 1
    return d

def main():
    s1 = input("Insert the first string\n")
    s2 = input("Insert the second string\n")
    r = ""
    if (anagrams(s1.upper())) != (anagrams(s2.upper())):
        r = "not "
    print(f"The strings '{s1}' and '{s2}' are {r}anagrams")


if __name__ == '__main__':
    main()
