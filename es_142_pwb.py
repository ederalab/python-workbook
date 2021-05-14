# unique characters

def unique_characters(s):
    d = {}
    i = 1
    for c in s:
        if c not in d:
            d[c] = i
        else:
            d[c] += 1

    unique = 0
    not_unique = 0
    for k in d:
        if d[k] == 1:
            unique += 1
        else:
            not_unique += 1

    count = unique + not_unique
    return count


def main():
    s = input("Insert a string and I'll count the unique characters\n")
    n = unique_characters(s)
    print(f"There are {n} unique values in your string")


if __name__ == '__main__':
    main()
