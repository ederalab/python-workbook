#pig latin

def pigLatin(s):
    s = s.lower()
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    result = ""

    #replace any symbols with a space
    for c in s:
        if c not in consonants and c not in vowels:
            s = s.replace(c, " ")

    #transform the string in a list
    t = s.split()

    for w in t:
        i = 0
        if w[0] in consonants:
            end = ""
            while i < len(w):
                if w[i] in vowels:
                    break
                end = end + w[i]
                i += 1
            new_word = w[slice(i, len(w))] + end + "ay"
        else:
            new_word = w + "way"
        result = result + new_word + " "

    return result


def main():
    string = input("Insert a string to translate in lating pig: ")
    print(pigLatin(string))


if __name__ == "__main__":
    main()
