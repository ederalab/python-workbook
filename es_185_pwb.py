# run-lenght decoding

def decoding(t, i = 0, new_list = []):
    if i < len(t) :
        if i % 2 != 0 :
            if t[i] != 0:
                new_list.append(t[i - 1])
                t[i] = t[i] - 1
            else:
                i += 1
        else:
            i += 1
        return decoding(t, i, new_list)
    return new_list


def main():
    t = ['A', 12, 'B', 4, 'A', 5, 'B', 1]
    print(decoding(t))


if __name__ == '__main__':
    main()