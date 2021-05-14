# run-lenght encoding

def encoding(t):
    if len(t) == 0:
        return []

    i = 1
    while i < len(t) and t[i] == t[i - 1]:
        i += 1

    encode = [t[0], i]
    return encode + encoding(t[i : len(t)])

def main():
    #t = ['A', 12, 'B', 4, 'A', 5, 'B', 1]
    t = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B']
    print(encoding(t))


if __name__ == '__main__':
    main()