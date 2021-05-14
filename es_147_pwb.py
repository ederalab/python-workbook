# checking for a winning card

def check_winning_card(card):
    mode = ""
    # vertical check
    for k in card:
        count = 0
        for n in card[k]:
            count = count + n
        if count == 0:
            mode = "vertical"
            return True, mode

    # horizontal check
    for ind in range(5):
        count = 0
        for k in card:
            count += card[k][ind]
        if count == 0:
            mode = "horizontal"
            return True, mode

    # diagonal check
    i = 0
    j = 4
    for k in card:
        if card[k][i] == 0:
            i += 1
        if card[k][j-1] == 0:
            j -= 1
    if i == 5 or j == 0:
        mode = "diagonal"
        return True, mode

    return False, mode


def display_card(card):
    keys = ["B", "I", "N", "G", "O"]
    for k in card:
        print(f"   {k} ", end="")
    print()

    for i in range(5):
        for letter in keys:
            print("%4d " % card[letter][i], end="")
        print()


def main():
    v_win = {
        'B': [14, 15, 0, 0, 13],
        'I': [21, 19, 25, 26, 20],
        'N': [0, 0, 0, 0, 0],
        'G': [48, 53, 0, 0, 0],
        'O': [71, 74, 62, 75, 73]
    }
    h_win = {
        'B': [14, 0, 11, 0, 10],
        'I': [21, 0, 25, 26, 0],
        'N': [43, 0, 42, 35, 0],
        'G': [0, 0, 57, 51, 0],
        'O': [71, 0, 0, 75, 0]
    }
    d1_win = {
        'B': [0, 15, 11, 3, 13],
        'I': [21, 0, 25, 26, 20],
        'N': [43, 36, 0, 35, 0],
        'G': [0, 53, 57, 0, 54],
        'O': [71, 74, 62, 75, 0]
    }
    d2_win = {
        'B': [14, 15, 11, 3, 0],
        'I': [21, 19, 25, 0, 20],
        'N': [43, 36, 0, 35, 0],
        'G': [48, 0, 57, 0, 54],
        'O': [0, 74, 62, 75, 0]
    }
    lose = {
        'B': [0, 15, 11, 3, 13],
        'I': [21, 22, 25, 26, 20],
        'N': [43, 36, 0, 35, 0],
        'G': [48, 0, 0, 0, 54],
        'O': [71, 74, 0, 0, 73]
    }

    cards = [v_win, h_win, d1_win, d2_win, lose]

    for i in range(len(cards)):
        print(f"********** CARD {i + 1} **********")

        display_card(cards[i])
        check, mode = check_winning_card(cards[i])

        print()

        if check:
            print(f"This card wins in a {mode} line!")
        else:
            print("This card lose!")

        print()


if __name__ == '__main__':
    main()
