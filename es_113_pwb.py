#avoiding duplicates
def removeDuplicates(t):
    #create an empty list where insert the values without duplicates
    dt = []
    for i in t:
        if i not in dt:
            dt.append(i)

    return dt

def main():
    user_list = []
    user_input = input("Insert a word (blank to quit): ")
    while user_input != "":
        user_list.append(user_input)
        user_input = input("Insert a word (blank to quit): ")

    new_list = removeDuplicates(user_list)
    for word in user_list:
        print(word)
    print("")
    for word in new_list:
        print(word)


if __name__ == "__main__":
    main()

