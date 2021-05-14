# reverse lookup

def reverseLookup(d, v):
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)

    return keys


def main():
    wine = {"grillo": "white", "nero d'avola": "red", "sangiovese": "red", "prosecco": "sparkling"}
    val = "red"
    result = reverseLookup(wine, val)
    print(val, "wines are:", result)


if __name__ == '__main__':
    main()
