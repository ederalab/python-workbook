#only the words

s = "that's my series of words! A long string, without any sense? Yes: without 'any' sense."
def onlyWords(s):
    s = s.replace(",", " ").replace(".", " ").replace(":", " ").replace(";", " ").replace("?", " ").replace("!", " ").replace(" '", " ").replace("' ", " ").replace('"', " ")
    t = s.split()
    return t

def main():
    user_string = input("Insert your string:\n")
    string_to_list = onlyWords(user_string)
    list_to_string = " ".join(string_to_list)
    print(list_to_string)


if __name__ == "__main__":
    main()