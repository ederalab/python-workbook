# is a list already in sorted order?

def is_sorted(t):
    asc = sorted(t)
    desc = list(reversed(asc))

    if t == asc or t == desc:
        return True
    else:
        return False

def main():
    t = []
    value = input("Insert some values in this list (blank to quit): ")
    while value != "":
        t.append(float(value))
        value = input("Insert some values in this list (blank to quit): ")

    if len(t) <= 1:
        print("It isn't possible to check because there are less than 2 values in the list")
        value = input("Insert some values in this list (blank to quit): ")
        t = []
        while value != "":
            t.append(float(value))
            value = input("Insert some values in this list (blank to quit): ")

    if is_sorted(t) == True:
        print(t)
        print("The list is sorted")
    else:
        print(t)
        print("The list is not in sorted order")


if __name__ == '__main__':
    main()

