#pig latin improved

def pigLatin(s):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    symbols = ["!", ".", ",", "'", "?", ":",'"',";"]
    result = ""

    #transform the string in a list
    t = s.split()

    for w in t:
        i = 0
        if w[0].lower() in consonants:
            end = ""
            while i < len(w):
                if w[i] in vowels:
                    break
                end = end + w[i].lower()
                i += 1
            new_word = w[slice(i, len(w))] + end + "ay"
        elif w[0].lower() in vowels:
            new_word = w + "way"
        if not w.islower():
            new_word = new_word.capitalize()
        result = result + new_word + " "

    t = result.split()

    result = []

    for w in t:
        i = 0
        add = ""
        new_word = w

        while i < len(w):
            if w[i] in symbols:
                add = w[i]
                w = w.replace(w[i],"")
                new_word = w + add
            i += 1
        result.append(new_word)

    result = " ".join(result)
    return result


def main():
    string = input("Insert a string to translate in lating pig: ")
    print(pigLatin(string))


if __name__ == "__main__":
    main()
