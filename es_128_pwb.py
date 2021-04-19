# count the elements

def countRange(t, min, max):
    i = 0
    for e in t:
        if e > min and e <= max:
            i += 1
    return i


def main():
    t =[]
    min = float(input("Insert the minimum value: "))
    max = float(input("Insert the maximum value: "))
    value = input("Insert the firtst value of the list (blank to quit):")
    while value != "":
        t.append(float(value))
        value = input("Insert the firtst value of the list (blank to quit):")

    result = countRange(t, min, max)
    print ("There are", result, "values in the list between", min, "and", max)


if __name__ == '__main__':
    main()