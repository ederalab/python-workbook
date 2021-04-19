# does a list contain a sublist?

def isSublist(l, s):
    if s == []:
        return True
    else:
        i = 0
        j = 0
        while l[i] != s[0]:
            i += 1

        while j < len(s):
            if l[i] != s[j]:
                return False
            j += 1
            i += 1
        return True


def main():
    l = []
    s = []

    user_list = input("Insert a larger list of elements (blank to quit): ")
    while user_list != "":
        l.append(user_list)
        user_list = input("Insert a larger list of elements (blank to quit): ")

    user_sublist = input("Insert a smaller list of elements (blank to quit): ")
    while user_sublist != "":
        s.append(user_sublist)
        user_sublist = input("Insert a smaller list of elements (blank to quit): ")

    result = isSublist(l, s)
    if result == True:
        print("The smaller list is a sublist of the larger one")
    else:
        print("The smaller list is not a sublist of the larger one")


if __name__ == '__main__':
    main()
