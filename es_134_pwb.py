# generate all sublist of a list

def createSublists(t):
    sublists = [[]]

    for s in range(1, len(t) + 1):
        for i in range(0, len(t) - s + 1):
            sublists.append(t[i : i + s])
    return sublists


def main():
    t = [1, 2, 3, 4, 5]
    print("The sublists of",t,"are:")
    result = createSublists(t)
    for i in range(0, len(result)):
        print(">>", result[i])


main()