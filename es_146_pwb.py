# create a bingo card
from random import randrange

def bingo_card():
    bingo = {}
    step = 15
    min = 1
    max = 1 + step
    keys = ["B", "I", "N", "G", "O"]

    for k in keys:
        bingo[k] = []
        while len(bingo[k]) != 5:
            n = randrange(min, max)
            if n not in bingo[k]:
                bingo[k].append(n)
        min = max + 1
        max = max + step
    return bingo


def main():
    bingo = bingo_card()
    keys = ["B", "I", "N", "G", "O"]
    for k in bingo:
        print(f"   {k} ", end="")
    print()

    for i in range(5):
        for letter in keys:
            print("%4d " % bingo[letter][i], end="")
        print()


if __name__ == '__main__':
    main()
