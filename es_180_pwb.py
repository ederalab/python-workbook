# string edit distance

def str_edit_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0

        if s[len(s)-1] != t[len(t)-1]:
            cost = 1

        d1 = str_edit_distance(s[0 : len(s) - 1], t) + 1
        d2 = str_edit_distance(s, t[0 : len(t) - 1]) + 1
        d3 = str_edit_distance(s[0 : len(s) - 1], t[0 : len(t) - 1]) + cost

        return min(d1, d2, d3)

def main():
    s1 = input("Insert the first string: ")
    s2 = input("Insert the second string: ")
    result = str_edit_distance(s1, s2)
    print("The edit distance between", s1, "and", s2, "is", result)

if __name__ == '__main__':
    main()


