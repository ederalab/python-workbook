#formatting a list

def formattedList(t):
    print(t[0], end="")
    i = 1
    while i < len(t) :
        separator = ","
        if i == len(t) - 1:
            separator = " and"
        print(separator, t[i], end="")
        i += 1


def main():
    user_list = []
    e = input("Insert an element in the list (blank to quit): \n")

    while e != "":
        user_list.append(e)
        e = input("Insert an element in the list (blank to quit): \n")

    formattedList(user_list)


if __name__ == "__main__":
    main()
